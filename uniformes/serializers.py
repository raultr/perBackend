from rest_framework import serializers
from .models import Uniforme
from uniformes_detalle.models import UniformeDetalle
from uniformes_detalle.serializers import UniformeDetalleSerializer

class UniformeSerializer(serializers.ModelSerializer):
	fecha =serializers.DateTimeField(format='%d/%m/%Y',input_formats=['%d/%m/%Y'])
	detalle_uniforme = UniformeDetalleSerializer(many=True, read_only=True)

	class Meta:
		model = Uniforme
		fields =('id','id_personal','fecha','fecha_servicio','anio','periodo','observaciones','detalle_uniforme')

	# def create(self, validated_data):
	# 	import ipdb;ipdb.set_trace()
	# 	uniforme_detalle_datos = validated_data.pop('detalle_uniforme')
	# 	uniforme = Uniforme.objects.create(**validated_data)
	# 	for detalle_datos in uniforme_detalle_datos:
	# 		UniformeDetalle.objects.create(uniforme=uniforme, **detalle_datos)
	# 	return uniforme