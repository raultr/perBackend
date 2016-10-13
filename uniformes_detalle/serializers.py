from rest_framework import serializers
from .models import UniformeDetalle
from catalogos_detalle.serializers import CatalogoSerializer

class UniformeDetalleSerializer(serializers.ModelSerializer):	
		class Meta:
			model = UniformeDetalle
			fields = ('id','uniforme','cdu_concepto_uniforme',)