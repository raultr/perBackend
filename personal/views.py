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
from .serializers import PersonalSerializer
from rest_framework.views import APIView
from .models import Personal


class PersonalOperaciones(APIView):
	def get_object(self, pk):
		try:
			return Personal.objects.get(pk=pk)
		except Personal.DoesNotExist:
			raise Http404


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

		serializer = PersonalSerializer(busqueda(valor_buscado), many=listado)
		return Response(serializer.data)

	def por_matricula(self,id_matricula):
		return get_object_or_404(Personal, matricula=id_matricula)
	
	def por_nombre(self,valor_buscado):
		qs = Personal.objects.all()
		for valor in valor_buscado.split():
			qs=qs.filter(Q(paterno__icontains = valor) | Q(materno__icontains = valor) | Q(nombre__icontains = valor) )
		return get_list_or_404(qs)

	def por_rfc(self,valor_buscado):
		return get_list_or_404(Personal,rfc__icontains = valor_buscado)