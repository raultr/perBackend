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
from .serializers import PersonalSucursalSerializer
from rest_framework.views import APIView
from .models import PersonalSucursal


class PersonalSucursalOperaciones(APIView):
	def get_object(self, id_perso):
		try:
			return PersonalSucursal.objects.get(id_personal=id_perso)
		except PersonalSucursal.DoesNotExist:
			raise Http404
	
	def get(self, request, id_perso=None, format=None):
		if(id_perso!=None):
			persuc = self.get_object(id_perso)
			serializer = PersonalSucursalSerializer(persuc)
			return Response(serializer.data)
		persuc = PersonalSucursal.objects.select_related()
		serializer = PersonalSucursalSerializer(persuc, many=True)
		return Response(serializer.data)