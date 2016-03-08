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
import datetime
from .serializers import IncidenciaSerializer
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models.deletion import ProtectedError
from .models import Incidencia


class IncidenciaOperaciones(APIView):
	#authentication_classes = (TokenAuthentication,)
	#permission_classes = (IsAuthenticated,)
	
	def get_object_por_id(self, id):
		try:
			return Incidencia.objects.select_related('cdu_concepto_incidencia','id_personal').filter(id_personal=id)
		except Incidencia.DoesNotExist:
			raise Http404

	def get(self, request,id_perso):
		incide = self.get_object_por_id(id_perso)
		serializer = IncidenciaSerializer(incide, many=True)
		return Response(serializer.data)

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