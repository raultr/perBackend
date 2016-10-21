from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from django.db import IntegrityError
from django.db.models import Q
from django.db import connection
import datetime
from django.utils.timezone import get_current_timezone


from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from .models import Permiso
from .serializers import PermisoSerializer,UsuarioSerializer
 
class PermisoAdministrador(APIView):
	#authentication_classes = (TokenAuthentication,)
	#permission_classes = (IsAuthenticated,)

	#def has_permission(self, request, view):
	#	MENU_PERMISOS = []
	#	permiso = request.user.groups.all().first()
	#	accesos = Permiso.objects.filter(rol=permiso.name).first()
	#	MENU_PERMISOS.append(accesos.permisos)
	#	return MENU_PERMISOS

	def has_permission(self, request, view):
		return request.user.groups.all().first()

	def get(self, request, format=None):
		permisos = self.has_permission(request,"")
		return Response({"Permiso": permisos.name})


class PermisoRolBuscar(APIView):
	#authentication_classes = (TokenAuthentication,)
	#permission_classes = (IsAuthenticated,)
	
	def get(self, request, rol_buscado):
		accesos = Permiso.objects.filter(rol=rol_buscado)
		serializer = PermisoSerializer(accesos, many=True)
		return Response(serializer.data)

class PermisoDatoUsuario(APIView):
	def get(self, request):
			usuario =  request.user;
			serializer = UsuarioSerializer(usuario)
			return Response(serializer.data)

