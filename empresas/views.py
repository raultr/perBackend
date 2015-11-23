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
from .serializers import EmpresaSerializer,PaginatedEmpresaSerializer,EmpresaRelacionSerializer
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db import IntegrityError
from .models import Empresa
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class EmpresaOperaciones(APIView):
	authentication_classes = (TokenAuthentication,SessionAuthentication)
	permission_classes = (IsAuthenticated,)
	
	def pre_save(self, obj):
		obj.owner = self.request.user

	def get_object(self, pk):
		try:
			return Empresa.objects.get(pk=pk)
		except Empresa.DoesNotExist:
			raise Http404

	def get(self, request, pk=None, format=None):
		if(pk!=None):
			empresa = self.get_object(pk)
			serializer = EmpresaSerializer(empresa)
			return Response(serializer.data)
		empresa = Empresa.objects.all()
		serializer = EmpresaSerializer(empresa, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		request.DATA['user'] =request.user.id
		serializer = EmpresaSerializer(data=request.DATA)
		if serializer.is_valid():
			try:
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			except IntegrityError as e:
				return Response({"La clave de la empresa ya existe"}, status=status.HTTP_403_FORBIDDEN)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def put(self, request, pk, format=None):
		request.DATA['user'] =request.user.id
		id = self.get_object(pk)
		serializer = EmpresaSerializer(id,data=request.DATA)
		print "Estoy validando"
		if serializer.is_valid():
			try:
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			except IntegrityError as e:
				return Response({"La clave de la empresa ya existe"}, status=status.HTTP_403_FORBIDDEN)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmpresaBusqueda(APIView):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)
	
	def get(self, request, valor_buscado):
		longitud = len(valor_buscado)
		#import ipdb; ipdb.set_trace()
		# Tupla de funciones de busqueda
		funciones_busqueda=(self.por_cve_empresa,self.por_razon_social,self.por_rfc)
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
		query = busqueda(valor_buscado)
		if i>0:
			paginator = Paginator(query, 10)

			page = request.QUERY_PARAMS.get('page')
			try:
				empr = paginator.page(page)
			except PageNotAnInteger:
				# If page is not an integer, deliver first page.
				empr = paginator.page(1)
			except EmptyPage:
				# If page is out of range (e.g. 9999),
				# deliver last page of results.
				empr = paginator.page(paginator.num_pages)
			serializer = PaginatedEmpresaSerializer(empr)
			return Response(serializer.data['results'])

		serializer = EmpresaSerializer(query)
		return Response(serializer.data)

	def por_cve_empresa(self,cve_empresa):
		return get_object_or_404(Empresa, cve_empresa=cve_empresa)
	
	def por_razon_social(self,valor_buscado):
		qs = Empresa.objects.all()
		qs = qs.filter(Q(razon_social__icontains = valor_buscado))
		return qs

	def por_rfc(self,valor_buscado):
		return get_list_or_404(Empresa,rfc__icontains = valor_buscado)

class EmpresaReportes(APIView):
	def get(self, request, pk=None, format=None):
		empresa = Empresa.objects.all()
		
		serializer = EmpresaRelacionSerializer(empresa, many=True)
		
		return Response(serializer.data)
