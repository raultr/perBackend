from rest_framework import serializers
from .models import Sucursal


class SucursalSerializer(serializers.ModelSerializer):
	cve_sucursal = serializers.IntegerField(required=False)
	fecha_alta =serializers.DateTimeField(format='%d/%m/%Y',input_formats=['%d/%m/%Y'])
	fecha_baja =serializers.DateTimeField(format='%d/%m/%Y',input_formats=['%d/%m/%Y'])

	def get_validation_exclusions(self, *args, **kwargs):
		exclusions = super(SucursalSerializer, self).get_validation_exclusions(*args, **kwargs)
		return exclusions + ['cve_sucursal']

	class Meta:
		model = Sucursal
		fields =('id', 'cve_empresa','cve_sucursal','nombre','calle','numero','colonia','cp',	'cdu_estado','cdu_municipio',
				'ciudad','telefono',	'cdu_estatus', 'fecha_alta','fecha_baja','latitud','longitud', )