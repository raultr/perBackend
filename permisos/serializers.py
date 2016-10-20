from rest_framework import serializers
from .models import Permiso

class PermisoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Permiso
		fields =('id','rol','permisos',)
