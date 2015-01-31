from rest_framework import serializers
from .models import CatalogoDetalle

class CatalogoSerializer(serializers.ModelSerializer):
		#iconos = serializers.Field('icono.url')
		#catalogos= serializers.RelatedField(many=False)
		class Meta:
			model = CatalogoDetalle
			#lookup_field = 'cdu_catalogo'
			fields = ( 'cdu_catalogo','num_dcatalogo','descripcion1','descripcion2',
				'monto1','monto2','cdu_default','catalogos')