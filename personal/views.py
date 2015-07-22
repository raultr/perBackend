import re
from django.shortcuts import render, get_object_or_404, get_list_or_404 
from django.http import Http404
from django.db import connection
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.parsers import FileUploadParser
from django.db.models import Q
from .serializers import PersonalSerializer,ImageSerializer,PaginatedPersonalSerializer
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework import parsers
from .models import Personal
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class ImageView(CreateAPIView):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	model = Personal
	#serializer_class = ImageSerializer
	#parser_classes = (parsers.MultiPartParser,)
	#parser_classes = (FileUploadParser,)

	
	def post(self, request, pk, format=None):
		photo = request.FILES['imagen']
		#id= Personal.objects.get(pk=pk)
		profile = Personal.objects.get(id=pk)
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
	
	def post(self, request):
		serializer = PersonalSerializer(data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
	def put(self, request, pk, format=None):
		id = self.get_object(pk)
		serializer = PersonalSerializer(id,data=request.DATA)
		print "Estoy validando"
		if serializer.is_valid():
			print "ya valide"
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
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
			paginator = Paginator(query, 2)

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
		return Response(serializer.data)
		
		

	def por_matricula(self,id_matricula):
		return get_object_or_404(Personal, matricula=id_matricula)
	
	def por_nombre(self,valor_buscado):
		qs = Personal.objects.all()
		for valor in valor_buscado.split():
			qs=qs.filter(Q(paterno__icontains = valor) | Q(materno__icontains = valor) | Q(nombre__icontains = valor) )
		return qs

	def por_rfc(self,valor_buscado):
		return get_list_or_404(Personal,rfc__icontains = valor_buscado)