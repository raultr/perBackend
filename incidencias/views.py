# -*- encoding: utf-8 -*-
import re
import json
from django.core.exceptions import ValidationError
from django.core.serializers.json import DjangoJSONEncoder
from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404, get_list_or_404 
from django.http import Http404
from django.db import connection
from rest_framework import status,viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.parsers import FileUploadParser
from django.db.models import F,Q
from datetime import datetime, date
import datetime
from .serializers import IncidenciaSerializer,IncidenciaRelacionSerializer
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models.deletion import ProtectedError
from .models import Incidencia
from personal_sucursales.models import PersonalSucursal

class IncidenciaNueva(APIView):
	#authentication_classes = (TokenAuthentication,)
	#permission_classes = (IsAuthenticated,)
	def get(self, request):
		incide = Incidencia.objects.all().order_by('-id')[:5]
		serializer = IncidenciaSerializer(incide, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		datos = request.DATA
		fecha = datetime.datetime.strptime(datos['fecha'],'%d/%m/%Y').strftime('%Y-%m-%d')
		fecha_activa = date(1900,1,1)
		#import ipdb; ipdb.set_trace()
		q = PersonalSucursal.objects.all()
		q = q.filter(Q(id_personal=datos['id_personal']),(Q(fecha_inicial__lte=fecha,fecha_final__gt=fecha)))
		datosAsignacion = q
		import ipdb; ipdb.set_trace()
		#q = q.filter(Q(id_personal=datos['id_personal']),(Q(fecha_inicial__lte=fecha,fecha_final__gt=fecha)|Q(fecha_inicial__lte=fecha,fecha_final=fecha_activa)))
		#import ipdb; ipdb.set_trace()
		#datosAsignacion = PersonalSucursal.objects.filter(id_personal=datos['id_personal'], fecha_inicial__lte=fecha,fecha_final__gt=fecha)
		#		q = Incidencia.objects.all()
		#	q = q.filter(Q(fecha__gte=fecha_ini,fecha__lte=fecha_fin), 
		#					Q(fecha__gte= F('id_personal__personalsucursal_id_personal__fecha_inicial'),fecha__lt= F('id_personal__personalsucursal_id_personal__fecha_final'))
		#					| Q(fecha__gte= F('id_personal__personalsucursal_id_personal__fecha_inicial') ,id_personal__personalsucursal_id_personal__fecha_final=fecha_activa)
		#					).values('id','id_personal__matricula','id_personal__paterno','id_personal__materno','id_personal__nombre',

		#import ipdb; ipdb.set_trace()
		if(len(datosAsignacion) == 0):
			return Response({"El elemento no esta asignado en esa fecha en ningun servicio"}, status=status.HTTP_403_FORBIDDEN)
		#datosAsignacion.cdu_motivo.cdu_catalogo
		#datosAsignacion= PersonalSucursal.objects.get(id_personal=datos['id_personal']).first()
		#print(datosAsignacion)
		serializer = IncidenciaSerializer(data=datos)
		if serializer.is_valid():
			try:
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			except Exception as e:
				return Response( e.args[0], status=status.HTTP_400_BAD_REQUEST)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IncidenciaModificacion(APIView):
	#authentication_classes = (TokenAuthentication,)
	#permission_classes = (IsAuthenticated,)
	
	def get_object_por_id(self, pk):
		try:
			return Incidencia.objects.select_related('cdu_concepto_incidencia','id_personal').filter(id=pk)
		except Incidencia.DoesNotExist:
			raise Http404

	def get(self, request,pk):
		incide = self.get_object_por_id(pk)
		serializer = IncidenciaSerializer(incide, many=True)
		return Response(serializer.data)

	def put(self, request, pk):
		datos = request.DATA
		fecha = datetime.datetime.strptime(request.DATA['fecha'],'%d/%m/%Y').strftime('%Y-%m-%d')
		incide_mod = Incidencia.objects.filter(id= pk, id_personal= datos['id_personal'],cdu_concepto_incidencia=datos['cdu_concepto_incidencia'],fecha=fecha)
		
		if(incide_mod.count() == 0):
			return Response({"Solo se puede modificar la observacion de una incidencia"}, status=status.HTTP_403_FORBIDDEN)
		incide_mod = Incidencia.objects.get(id=pk)	
		serializer = IncidenciaSerializer(incide_mod,data=request.DATA)
		if serializer.is_valid():
			try:
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			except IntegrityErrotransaction as e:
				return Response({"Ya existe esa incidencia"}, status=status.HTTP_403_FORBIDDEN)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
			try:
				suc_del = Incidencia.objects.get(pk=pk)
				suc_del.delete()
				return Response({"Exito"}, status=status.HTTP_201_CREATED)
			except Exception as e:
					return Response( e.args[0], status=status.HTTP_400_BAD_REQUEST)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class IncidenciaPersonalFecha(APIView):	
	def get_object_por_id(self, id, fecha_incide):
		fecha_formato =datetime.datetime.strptime(fecha_incide,'%d-%m-%Y').strftime('%Y-%m-%d')
		try:
			return Incidencia.objects.select_related('cdu_concepto_incidencia','id_personal').filter(id_personal=id, fecha= fecha_formato)
		except Incidencia.DoesNotExist:
			raise Http404

	def get(self, request,id_perso,fecha_incide):
		incide = self.get_object_por_id(id_perso,fecha_incide)
		serializer = IncidenciaSerializer(incide, many=True)
		return Response(serializer.data)

class IncidenciaConsulta(APIView):
	#authentication_classes = (TokenAuthentication,)
	#permission_classes = (IsAuthenticated,)
	
	def get_object_por_id(self, pk):
		try:
			return Incidencia.objects.select_related('cdu_concepto_incidencia','id_personal').filter(id=pk)
		except Incidencia.DoesNotExist:
			raise Http404

	def get(self, request):
		fecha_ini =datetime.datetime.strptime(request.GET['fecha_ini'],'%d/%m/%Y').strftime('%Y-%m-%d')
		fecha_fin =datetime.datetime.strptime(request.GET['fecha_fin'],'%d/%m/%Y').strftime('%Y-%m-%d')
		fecha_activa = date(1900,1,1)
		try:
			q = Incidencia.objects.all()
			q = q.filter(Q(fecha__gte=fecha_ini,fecha__lte=fecha_fin), 
							Q(fecha__gte= F('id_personal__personalsucursal_id_personal__fecha_inicial'),fecha__lt= F('id_personal__personalsucursal_id_personal__fecha_final'))
							| Q(fecha__gte= F('id_personal__personalsucursal_id_personal__fecha_inicial') ,id_personal__personalsucursal_id_personal__fecha_final=fecha_activa)
							).values('id','id_personal__matricula','id_personal__paterno','id_personal__materno','id_personal__nombre',
							'fecha','observaciones','cdu_concepto_incidencia','cdu_concepto_incidencia__descripcion1',
							'id_personal__personalsucursal_id_personal__cdu_turno','id_personal__personalsucursal_id_personal__cdu_turno__descripcion1',
							'id_personal__personalsucursal_id_personal__cdu_puesto','id_personal__personalsucursal_id_personal__cdu_puesto__descripcion1',
							'id_personal__personalsucursal_id_personal__id_sucursal','id_personal__personalsucursal_id_personal__id_sucursal__nombre')

			columnas = {'id':'id','id_personal__matricula':'matricula','id_personal__paterno':'paterno',
						'id_personal__materno':'materno','id_personal__nombre':'nombre',
						'fecha':'fecha','observaciones':'observaciones',
						'cdu_concepto_incidencia':'cdu_incidencia','cdu_concepto_incidencia__descripcion1':'incidencia',
						'id_personal__personalsucursal_id_personal__cdu_turno':'cdu_turno','id_personal__personalsucursal_id_personal__cdu_turno__descripcion1':'turno',
						'id_personal__personalsucursal_id_personal__cdu_puesto':'cdu_puesto','id_personal__personalsucursal_id_personal__cdu_puesto__descripcion1':'puesto',
						'id_personal__personalsucursal_id_personal__id_sucursal':'id_sucursal','id_personal__personalsucursal_id_personal__id_sucursal__nombre':'sucursal'}

			reporte = []
			for diccionario in q:
				reporte.append(dict((columnas[key], value) for (key, value) in diccionario.items()))

			return Response(reporte)
		except Incidencia.DoesNotExist:
			raise Http404


		#serializer = IncidenciaSerializer(incide, many=True)
		#return Response(serializer.data)
		return Response(fecha_ini + ' : ' + fecha_fin)

#def viewname(request):
#    price_lte = request.GET['price_lte']
#    #Code to filter products whose price is less than price_lte i.e. 5000
# http://localhost:8001/incidencias/consulta/?fecha_ini=01/01/2016&fecha_fin=01/01/2016
# http://localhost:8001/incidencias/consulta/?fecha_ini=18/03/2016&fecha_fin=19/03/2016