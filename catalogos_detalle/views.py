from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.parsers import FileUploadParser
from .serializers import CatalogoSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import CatalogoDetalle
	
@api_view(['GET', 'POST'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def request_response_list(request,id_catalogo):
	if request.method == 'GET':
		catalogo_detalle= get_list_or_404(CatalogoDetalle, catalogos=id_catalogo)
		serializer = CatalogoSerializer(catalogo_detalle, many=True)
		return Response(serializer.data)

@api_view(['GET','PUT','POST'])
#@authentication_classes((TokenAuthentication,))
#@permission_classes((IsAuthenticated,))
def request_response_detalle(request,id_catalogo):
	if request.method == 'GET':
		listado = id_catalogo.split(',')
		catalogo_detalle=CatalogoDetalle.objects.filter(catalogos__in=listado)
		#catalogo_detalle= get_list_or_404(CatalogoDetalle, catalogos=[1,12,3])
		serializer = CatalogoSerializer(catalogo_detalle, many=True)
		return Response(serializer.data)
	if request.method == 'PUT':
		id = CatalogoDetalle.objects.get(pk=id_catalogo)
		serializer = CatalogoSerializer(id,data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	if request.method == 'POST':
		serializer = CatalogoSerializer(data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT'])
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def request_response_detalle_cdu_default(request,id_catalogo,cdu_default):
	if request.method == 'GET':
		listado = id_catalogo.split(',')
		catalogo_detalle=CatalogoDetalle.objects.filter(catalogos__in=listado,cdu_default=cdu_default)
		#catalogo_detalle= get_list_or_404(CatalogoDetalle, catalogos=[1,12,3])
		serializer = CatalogoSerializer(catalogo_detalle, many=True)
		return Response(serializer.data)


@api_view(['POST'])
#@authentication_classes((TokenAuthentication,))
#@permission_classes((IsAuthenticated,))
def request_response_nuevo(request):
	if request.method == 'POST':
		serializer = CatalogoSerializer(data=request.DATA, many=True)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
