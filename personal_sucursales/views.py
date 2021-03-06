# -*- encoding: utf-8 -*-
import re
import json
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
from django.db.models import Q
from datetime import datetime, date
import datetime
from .serializers import PersonalSucursalSerializer,PersonalSucursalSerializerSimple,PersonalSucursalSerializerPersonal,PersonalSucursalSerializerAsignacion
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models.deletion import ProtectedError
from .models import PersonalSucursal


class PersonalSucusalMenu(APIView):	
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	
	def get(self,request, pk=None, format=None):
		data = {"personal_sucursal":"Si"}
		return Response(data,status=status.HTTP_201_CREATED)

class PersonalSucursalConsultas(APIView):
	#authentication_classes = (TokenAuthentication,)
	#permission_classes = (IsAuthenticated,)
	def get_object_persona_sucursal_activa(self, id_perso):
		try:
			return PersonalSucursal.objects.select_related('id_sucursal','cdu_motivo','cdu_turno','cdu_puesto','cdu_rango').get(id_personal=id_perso,fecha_final="1900-01-01")
		except PersonalSucursal.DoesNotExist:
			raise Http404
	def get_object_sucursal_personal_activo(self, id_sucursal):
		try:
			return PersonalSucursal.objects.select_related('id_personal').filter(id_sucursal__cve_sucursal=id_sucursal,fecha_final="1900-01-01")
		except PersonalSucursal.DoesNotExist:
			raise Http404

	def get(self, request, id_perso=None,id_sucursal=None, format=None):
		if(id_perso!=None):
			persuc = self.get_object_persona_sucursal_activa(id_perso)
			serializer = PersonalSucursalSerializer(persuc)
			return Response(serializer.data)
		if(id_sucursal!=None):
			sucpersonal = self.get_object_sucursal_personal_activo(id_sucursal)
			serializer = PersonalSucursalSerializerPersonal(sucpersonal, many=True)
			return Response(serializer.data)
		persuc = PersonalSucursal.objects.select_related()
		serializer = PersonalSucursalSerializer(persuc, many=True)
		return Response(serializer.data)


class PersonalSucursalOperaciones(APIView):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	
	def get_object_por_id(self, id):
		try:
			return PersonalSucursal.objects.select_related('id_sucursal','cdu_motivo','cdu_turno','cdu_puesto','cdu_rango').get(id=id)
		except PersonalSucursal.DoesNotExist:
			raise Http404
	
	def get(self, request):
		persuc = PersonalSucursal.objects.select_related()
		serializer = PersonalSucursalSerializer(persuc, many=True)
		return Response(serializer.data)

	def post(self, request):
		request.DATA['user'] =request.user.id
		serializer = PersonalSucursalSerializerSimple(data=request.DATA)
		if serializer.is_valid():	
			try:	
				serializer.save()
				persuc = self.get_object_por_id(serializer.data['id'])
				serializer = PersonalSucursalSerializer(persuc)
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			except ValidationError as e:
				return Response(e.message, status=status.HTTP_400_BAD_REQUEST)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		try:
			persuc_del = PersonalSucursal.objects.get(pk=pk, fecha_final="1900-01-01")
			#persuc_del.user = request.user
			#persuc_del.save()
			persuc_del.delete()
			#PersonalSucursal.objects.get(pk=pk, fecha_final="1900-01-01").delete()
			return Response({"Exito"}, status=status.HTTP_201_CREATED)
		except ValidationError as e:
				return Response(e.message, status=status.HTTP_400_BAD_REQUEST)
		except ProtectedError as e:
				return Response({"Esta sucursal tiene asignaciones y no puede ser eliminada"}, status=status.HTTP_403_FORBIDDEN)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonalSucursalReportes(APIView):
	def get(self, request,id_empresa):
		listado = id_empresa.split(',')
		queryset = PersonalSucursal.objects.values('id','sueldo','id_personal','id_personal__matricula','id_personal__nombre','id_personal__paterno','id_personal__materno',
												'id_sucursal__cve_empresa','id_sucursal__cve_empresa__cve_empresa','id_sucursal__cve_empresa__razon_social',
												'id_sucursal__id','id_sucursal__cve_sucursal','id_sucursal__nombre','cdu_puesto','cdu_puesto__descripcion1',
												'cdu_rango__descripcion1','cdu_turno__descripcion1','cdu_motivo','cdu_motivo__descripcion1').select_related().filter(id_sucursal__cve_empresa__in=listado, fecha_final="1900-01-01")
		serialized = json.dumps(list(queryset), cls=DjangoJSONEncoder)#DjangoJSONEncoder para que se lleve bien con fechas y decimales
		return Response(list(queryset))

class PersonalSucursalFecha(APIView):	
	def get_object_por_id(self, id_personal, fecha):
		try:
			fecha_activa = date(1900,1,1)
			fecha =datetime.datetime.strptime(fecha,'%d-%m-%Y').strftime('%Y-%m-%d')
			q = PersonalSucursal.objects.all()
			q = q.filter(Q(id_personal=id_personal),(Q(fecha_inicial__lte=fecha,fecha_final__gt=fecha)|Q(fecha_inicial__lte=fecha,fecha_final=fecha_activa)))	
			return q
		except:
			raise Http404

	def get(self, request,id_perso,fecha_asignacion):
		asignacion = self.get_object_por_id(id_perso,fecha_asignacion)
		serializer = PersonalSucursalSerializerAsignacion(asignacion, many=True)
		return Response(serializer.data)