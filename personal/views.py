import re
from django.shortcuts import render, get_object_or_404, get_list_or_404 
from django.http import Http404
from django.db import connection
from django.db.models.deletion import ProtectedError
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.parsers import FileUploadParser
from django.db import transaction
from django.db.models import Q
from .serializers import PersonalSerializer,ImageSerializer,PaginatedPersonalSerializer
from personal_sucursales.serializers import PersonalSucursalSerializerSimple
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework import parsers
from .models import Personal
from personal_sucursales.models import PersonalSucursal
from catalogos_detalle.models import CatalogoDetalle
from personal_sucursales.models import PersonalSucursal
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db import IntegrityError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class ImageView(CreateAPIView):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	model = Personal
	EXTENCIONES_VALIDAS = [".jpg",".jpeg"]
	VALID_IMAGE_MIMETYPES = ["image"]
	#serializer_class = ImageSerializer
	#parser_classes = (parsers.MultiPartParser,)
	#parser_classes = (FileUploadParser,)

	def valid_url_extension(self,archivo, extension_list=EXTENCIONES_VALIDAS):
		return any([archivo.endswith(e) for e in extension_list])
	
	def post(self, request, pk, format=None):
		photo = request.FILES['imagen']
		if not(self.valid_url_extension(photo.name.lower())):
			data ={"message":"El archivo no es una imagen"}
			return Response(data,status=status.HTTP_403_FORBIDDEN)	
		if(photo.size>1010661):
			data ={"message":"La foto no debe de ser mayor a 1 mb"}
			return Response(data,status=status.HTTP_403_FORBIDDEN)	
		#id= Personal.objects.get(pk=pk)
		profile = Personal.objects.get(id=pk)
		photo.name = str(pk) + '.jpg'  #+ "." + photo.name.split(".")[1]
		profile.imagen = photo
		profile.save()
		#serializer = ImageSerializer(id,data=request.DATA)		
		#personal = self.get_object(pk)
		#personal.imagen = photo
		#serializer.imagen = photo
		#print serializer.imagen
		#serializer.save()
		data    = ImageSerializer(profile).data
		return Response(data, status=status.HTTP_201_CREATED)
		#parser_classes = (parsers.FileUploadParser,)


class PersonalMenu(APIView):	
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)

	def get(self,request, pk=None, format=None):
		#import ipdb;ipdb.set_trace();
		data = {"personal":"Si"}
		return Response(data,status=status.HTTP_201_CREATED)

class PersonalOperaciones(APIView):	
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)

	def get_object(self, pk):
		try:
			return Personal.objects.get(pk=pk)
		except Personal.DoesNotExist:
			raise Http404

	def get(self, request, pk=None, format=None):
		if(pk!=None):
			personal = self.get_object(pk)
			serializer = PersonalSerializer(personal)
			return Response(serializer.data)
		personal = Personal.objects.all()
		serializer = PersonalSerializer(personal, many=True)
		return Response(serializer.data)
	
	@transaction.atomic
	def post(self, request):
		request.DATA['personal'][0]['user'] =request.user.id
		serializer = PersonalSerializer(data=request.DATA['personal'][0])
		if serializer.is_valid():
			try:
				sid = transaction.savepoint()
				nuevaPersona = serializer.save()	
				datos_asignacion = request.DATA['asignacion'][0]
				datos_asignacion['id_personal'] =  nuevaPersona.id
				datos_asignacion['cdu_motivo'] =  '0250000'
				datos_asignacion['fecha_inicial'] = nuevaPersona.fec_alta
				datos_asignacion['fecha_final'] = '01/01/1900'
				datos_asignacion['motivo'] = "Alta del personal"
				serializer_asignacion =PersonalSucursalSerializerSimple(data=datos_asignacion)			
				if serializer_asignacion.is_valid():
					print "voy a guardar"
					nuevaAsignacion= serializer_asignacion.save()
				else:
					print "no es valido"
					transaction.savepoint_rollback(sid)
					return Response(serializer_asignacion.errors, status=status.HTTP_403_FORBIDDEN)
				transaction.savepoint_commit(sid)
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			except IntegrityError as e:
				print "error de IntegrityError"
				transaction.savepoint_rollback(sid)
				return Response({"La matricula ya existe"}, status=status.HTTP_403_FORBIDDEN)
			except Exception as e:
				print "error de Exception"
				transaction.savepoint_rollback(sid)
				return Response(e.message, status=status.HTTP_403_FORBIDDEN)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
	def put(self, request, pk, format=None):
		request.DATA['personal'][0]['user'] =request.user.id
		id = self.get_object(pk)
		serializer = PersonalSerializer(id,data=request.DATA['personal'][0])
		if serializer.is_valid():
			try:
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			except IntegrityError as e:
				return Response({"La matricula ya existe"}, status=status.HTTP_403_FORBIDDEN)
			except Exception as e:
				print e
				return Response(e.message, status=status.HTTP_403_FORBIDDEN)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		try:
			per_del = Personal.objects.get(pk=pk)
			per_del.user = request.user
			per_del.save()
			per_del.delete()
			#Personal.objects.get(pk=pk).delete()
			return Response({"Exito"}, status=status.HTTP_201_CREATED)
		except ProtectedError as e:
				return Response({"Esta persona tiene asignaciones y no puede ser borrada"}, status=status.HTTP_403_FORBIDDEN)
		except Exception as e:
				return Response( e.args[0], status=status.HTTP_400_BAD_REQUEST)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	
class PersonalBusqueda(APIView):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	
	def get(self, request, valor_buscado):
		longitud = len(valor_buscado)
		#import ipdb; ipdb.set_trace()
		# Tupla de funciones de busqueda
		funciones_busqueda=(self.por_matricula,self.por_nombre,self.por_rfc)
		# La expresion regular esta relacionada una una con la tupla de campos
		exp_reg=("[0-9]{%s,}"%(longitud),"[A-Za-z\s]{%s,}"%(longitud),"[A-Za-z0-9]{%s,}"%(longitud))
		# Buscamos con cual expresion regular concuerda la url para saber funcion de buscar se utilizara
		i=0
		listado = False
		for exp in exp_reg:
			if(re.match(exp,valor_buscado)):
				break
			i+=1
			listado = True
		# la posicion la funcion de busqueda que se utilizara
		busqueda = funciones_busqueda[i]

		#serializer = PersonalSerializer(busqueda(valor_buscado), many=listado)
		query = busqueda(valor_buscado)
		if i>0:
			paginator = Paginator(query, 10)

			page = request.QUERY_PARAMS.get('page')
			try:
				perso = paginator.page(page)
			except PageNotAnInteger:
				# If page is not an integer, deliver first page.
				perso = paginator.page(1)
			except EmptyPage:
				# If page is out of range (e.g. 9999),
				# deliver last page of results.
				perso = paginator.page(paginator.num_pages)
			serializer = PaginatedPersonalSerializer(perso)
			return Response(serializer.data['results'])
		serializer = PersonalSerializer(query)
		act =self.EstaActivo(serializer.data['id'])
		estatus = ''
		print act
		if(act is None):
			estatus ='Inactivo'
		elif(act['cdu_motivo']=='0250003'):
			estatus = 'Baja'
		print estatus
		serializer.data['estatus']=estatus
		#'cdu_motivo' 0250000
		#import ipdb;ipdb.set_trace()
		#print(serializer.data['results'])
		#return Response(query[0])
		return Response(serializer.data)

	def EstaActivo(self,id):
		qs =PersonalSucursal.objects.filter(id_personal__id=id,fecha_final="1900-01-01")
		if(len(qs)==0):
			return None
		serializer = PersonalSucursalSerializerSimple(qs[0])
		return serializer.data		

	def por_matricula(self,id_matricula):
		return get_object_or_404(Personal, matricula=id_matricula)
		#qs = Personal.objects.all()
		#qs= Personal.objects.filter(Q(personalsucursal_id_personal__isnull=True) | Q(personalsucursal_id_personal__isnull=False), Q(personalsucursal_id_personal__fecha_final='1900-01-01') | Q(personalsucursal_id_personal__fecha_final__isnull=True),matricula=id_matricula)
		#qs=Personal.objects.only('id','matricula','paterno','materno','nombre','rfc','curp','cuip','fec_nacimiento','cdu_estado_nac','cdu_municipio_nac','cdu_estado_civil','cdu_escolaridad','cdu_seguridad_social','id_seguridad_social','portacion','cdu_tipo_alta','fec_alta','condicionada','condiciones_alta','cdu_tipo_empleado','calle_dom','numero_dom','colonia_dom','cp_dom','cdu_estado_dom','cdu_municipio_dom','imagen').filter(Q(personalsucursal_id_personal__isnull=True) | Q(personalsucursal_id_personal__isnull=False), Q(personalsucursal_id_personal__fecha_final='1900-01-01') | Q(personalsucursal_id_personal__fecha_final__isnull=True),matricula=id_matricula).select_related('personalsucursal_id_personal')
		#qs=Personal.objects.filter(Q(personalsucursal_id_personal__isnull=True) | Q(personalsucursal_id_personal__isnull=False), Q(personalsucursal_id_personal__fecha_final='1900-01-01') | Q(personalsucursal_id_personal__fecha_final__isnull=True),matricula=id_matricula).select_related('personalsucursal_id_personal').defer('personalsucursal_id_personal_cdu_turno')
		#import ipdb;ipdb.set_trace()
		#serializer = PersonalSerializer(qs[0])
		#return qs
	
	def por_nombre(self,valor_buscado):
		qs = Personal.objects.all()
		for valor in valor_buscado.split():
			qs=qs.filter(Q(paterno__icontains = valor) | Q(materno__icontains = valor) | Q(nombre__icontains = valor) )
		return qs

	def por_rfc(self,valor_buscado):
		return get_list_or_404(Personal,rfc__icontains = valor_buscado)