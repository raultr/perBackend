from rest_framework import serializers
from .models import Empresa

class EmpresaSerializer(serializers.ModelSerializer):
		empresas_detalle = serializers.RelatedField(many=True)
		class Meta:
			model = Empresa
			
			fields = ('id_empresa','razon_social','rfc','calle','numero','colonia','cp','cdu_estado','cdu_giro',
				'cdu_municipio','ciudad','telefono1','telefono2','cdu_giro','cdu_rubro','fecha_alta',)