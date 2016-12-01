from rest_framework import serializers
from .models import UniformeDetalle
from catalogos_detalle.serializers import CatalogoSerializer

class UniformeDetalleSerializer(serializers.ModelSerializer):	
		class Meta:
			model = UniformeDetalle
			fields = ('id','uniforme','cdu_concepto_uniforme',)


class UniformeDetalleSerializerDescripcion(serializers.ModelSerializer):	
		cdu_concepto_uniforme = CatalogoSerializer(many=True, read_only=True)

		class Meta:
			model = UniformeDetalle
			fields = ('id','uniforme','cdu_concepto_uniforme',)