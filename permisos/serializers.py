from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Permiso

class PermisoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Permiso
		fields =('id','rol','permisos',)

class UsuarioSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields =('id','first_name','last_name',)
