from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, date
import datetime
from django.db import IntegrityError
from django.db import transaction
from .models import Uniforme
from uniformes_detalle.models import UniformeDetalle
from catalogos_detalle.models import CatalogoDetalle
from .serializers import UniformeSerializer
from .serializers import UniformeDetalleSerializer
# Create your views here.

class UniformeConDetallesLista(APIView):
	def get(self, request, pk=None, format=None):
		if(pk!=None):
			print(pk)

		queryset = Uniforme.objects.all()
		serializer_class = UniformeSerializer(queryset,many=True)
		return  Response(serializer_class.data)
	
	def post(self, request, format=None):
		serializer_class = UniformeSerializer(data=request.DATA)
		if serializer_class.is_valid():
			try:
				with transaction.atomic():
					datos = request.DATA
					uniformes= Uniforme.objects.filter(id_personal=datos['id_personal'],anio=datos['anio'],periodo=datos['periodo'])
					if uniformes.first():
						uniforme = uniformes.first()
						uniforme.observaciones = datos['observaciones']
						uniforme.fecha = datetime.datetime.strptime(datos['fecha'],'%d/%m/%Y').strftime('%Y-%m-%d')
						uniforme.save()
					else:
						response = serializer_class.save()
						uniforme = Uniforme.objects.get(id=response.id)	
						
					UniformeDetalle.objects.filter(uniforme=uniforme.pk).delete()
					uniforme_detalle_datos = request.DATA.pop('detalle_uniforme')
					for detalle_datos in uniforme_detalle_datos:
						catalogo_uniforme = CatalogoDetalle.objects.get(cdu_catalogo=detalle_datos['cdu_concepto_uniforme'])
						UniformeDetalle.objects.create(uniforme=uniforme,cdu_concepto_uniforme=catalogo_uniforme)

					queryset = Uniforme.objects.filter(pk=uniforme.pk)
					datos =  UniformeSerializer(queryset,many=True)

				return Response(datos.data, status=status.HTTP_201_CREATED)
			except IntegrityError as ex:
				return Response({'error': str(ex)}, status=status.HTTP_403_FORBIDDEN)
			except Exception as ex:
				return Response({'error': str(ex)}, status=status.HTTP_403_FORBIDDEN)
		return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonalUniformeConDetalles(APIView):
	def get(self, request, pk=None, format=None):
		campos = {}
		if 'id_personal' in request.GET:
			campos['id_personal'] = request.GET['id_personal']
		if 'anio' in request.GET:
			campos['anio'] = request.GET['anio']
		if 'periodo' in request.GET:
			campos['periodo'] = request.GET['periodo']
		queryset = Uniforme.objects.filter(**campos )
		serializer_class = UniformeSerializer(queryset,many=True)
		return  Response(serializer_class.data)
