import re
from django.shortcuts import render, get_object_or_404, get_list_or_404 
from django.http import Http404
from django.db import connection
from rest_framework import status,viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.parsers import FileUploadParser
from django.db.models import Q
from .serializers import PersonalSucursalSerializer,PersonalSucursalSerializerSimple
from rest_framework.views import APIView
from .models import PersonalSucursal


class PersonalSucursalOperaciones(APIView):
	def get_object_por_id(self, id):
		try:
			return PersonalSucursal.objects.select_related('id_sucursal','cdu_motivo','cdu_turno','cdu_puesto','cdu_rango').get(id=id)
		except PersonalSucursal.DoesNotExist:
			raise Http404
	
	def get_object_por_persona(self, id_perso):
		try:
			return PersonalSucursal.objects.select_related('id_sucursal','cdu_motivo','cdu_turno','cdu_puesto','cdu_rango').get(id_personal=id_perso)
		except PersonalSucursal.DoesNotExist:
			raise Http404

	
	def get(self, request, id_perso=None, format=None):
		if(id_perso!=None):
			persuc = self.get_object_por_persona(id_perso)
			serializer = PersonalSucursalSerializer(persuc)
			return Response(serializer.data)
		persuc = PersonalSucursal.objects.select_related()
		serializer = PersonalSucursalSerializer(persuc, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = PersonalSucursalSerializerSimple(data=request.DATA)
		if serializer.is_valid():		
			serializer.save()
			persuc = self.get_object_por_id(serializer.data['id'])
			serializer = PersonalSucursalSerializer(persuc)
			#serializer.data['id_sucursal']
			#import ipdb; ipdb.set_trace()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)