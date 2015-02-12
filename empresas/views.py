from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.parsers import FileUploadParser
from .serializers import EmpresaSerializer
from .models import Empresa
	
	
	
@api_view(['GET', 'POST'])
def request_response_list(request):
	if request.method == 'GET':
		empresas = Empresa.objects.all()
		serializer = EmpresaSerializer(empresas, many=True)
		return Response(serializer.data)
	
	elif request.method == 'POST':
		serializer = EmpresaSerializer(data=request.DATA)
		#import ipdb; ipdb.set_trace()
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)