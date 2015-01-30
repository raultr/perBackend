import re
from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.parsers import FileUploadParser
from django.db.models import Q
from .serializers import PersonalSerializer
from rest_framework.views import APIView
from .models import Personal
	
class PersonalBusqueda(APIView):
	def get(self, request, valor_buscado):
		longitud = len(valor_buscado)
		exp_reg=("[0-9]{%s,}"%(longitud),"[A-Za-z\s]{%s,}"%(longitud),"[A-Za-z0-9]{%s,}"%(longitud))
		#import ipdb; ipdb.set_trace()
		funciones_busqueda=(self.por_matricula,self.por_nombre,self.por_rfc)

		i=0
		listado = False
		for exp in exp_reg:
			if(re.match(exp,valor_buscado)):
				break
			i+=1
			listado = True

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

	def post(self, request, format=None):
		serializer = PersonalSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)