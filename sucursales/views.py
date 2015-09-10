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
from .serializers import SucursalSerializer
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db import IntegrityError
from django.db.models.deletion import ProtectedError
from .models import Sucursal

class SucursalMenu(APIView):	
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	def get(self,request, pk=None, format=None):
		#import ipdb;ipdb.set_trace();
		data = {"sucursal":"Si"}
		return Response(data,status=status.HTTP_201_CREATED)

class SucursalOperaciones(APIView):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	def get_object(self, pk):
		try:
			return Sucursal.objects.get(pk=pk)
		except Sucursal.DoesNotExist:
			raise Http404

	def get(self, request, pk=None, format=None):
		if(pk!=None):
			sucursal = self.get_object(pk)
			serializer = SucursalSerializer(sucursal)
			return Response(serializer.data)
		sucursal = Sucursal.objects.all()
		serializer = SucursalSerializer(sucursal, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = SucursalSerializer(data=request.DATA)
		if serializer.is_valid():
			try:
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			except IntegrityError as e:
				return Response({"La clave de sucursal ya existe"}, status=status.HTTP_403_FORBIDDEN)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
	def put(self, request, pk, format=None):
		id = self.get_object(pk)
		serializer = SucursalSerializer(id,data=request.DATA)
		if serializer.is_valid():
			try:
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			except IntegrityError as e:
				return Response({"La clave de sucursal ya existe"}, status=status.HTTP_403_FORBIDDEN)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		try:
			Sucursal.objects.get(pk=pk).delete()
			return Response({"Exito"}, status=status.HTTP_201_CREATED)
		except ProtectedError as e:
				return Response({"Esta sucursal tiene asignaciones y no puede ser eliminada"}, status=status.HTTP_403_FORBIDDEN)
		except Exception as e:
				return Response( e.args[0], status=status.HTTP_400_BAD_REQUEST)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SucursalesEmpresa(APIView):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	def get(self,request,id_empresa,format=None):
		sucursal = get_list_or_404(Sucursal.objects.order_by('cve_sucursal'), cve_empresa=id_empresa)
		serializer = SucursalSerializer(sucursal,many=True)
		
		return Response(serializer.data)

class SucursalBusqueda(APIView):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	def get(self, request, valor_buscado):
		longitud = len(valor_buscado)
		#import ipdb; ipdb.set_trace()
		# Tupla de funciones de busqueda
		funciones_busqueda=(self.por_cve_sucursal,self.por_nombre)
		# La expresion regular esta relacionada una una con la tupla de campos
		exp_reg=("[0-9]{%s,}"%(longitud),"[A-Za-z\s]{%s,}"%(longitud))
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

		serializer = SucursalSerializer(busqueda(valor_buscado), many=listado)
		return Response(serializer.data)

	def por_cve_sucursal(self,cve_sucursal):
		return get_object_or_404(Sucursal, cve_sucursal=cve_sucursal)
	
	def por_nombre(self,valor_buscado):
		qs = Sucursal.objects.all()
		qs = qs.filter(Q(nombre__icontains = valor_buscado))
		return get_list_or_404(qs)