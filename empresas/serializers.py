from rest_framework import serializers
from .models import Empresa


class EmpresaSerializer(serializers.ModelSerializer):
	cve_empresa = serializers.IntegerField(required=False)
	fecha_alta =serializers.DateTimeField(format='%d/%m/%Y',input_formats=['%d/%m/%Y'])

	def get_validation_exclusions(self, *args, **kwargs):
		exclusions = super(EmpresaSerializer, self).get_validation_exclusions(*args, **kwargs)
		return exclusions + ['cve_empresa']

	class Meta:
		model = Empresa
		fields = ('id','cve_empresa','razon_social','rfc','calle','numero','colonia','cp','cdu_estado','cdu_giro',
				'cdu_municipio','telefono1','telefono2','cdu_giro','cdu_rubro','fecha_alta','latitud','longitud',)					