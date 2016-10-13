from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UniformeDetalle
from .serializers import UniformeDetalleSerializer
# Create your views here.

class UniformeDetalleConDetallesLista(APIView):
	def get(self, request, pk=None, format=None):
		if(pk!=None):
			print(pk)

		queryset = UniformeDetalle.objects.all()
		serializer_class = UniformeDetalleSerializer(queryset,many=True)
		return  Response(serializer_class.data)

