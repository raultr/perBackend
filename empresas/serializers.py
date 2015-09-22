from rest_framework import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Empresa
from rest_framework import pagination


class EmpresaSerializer(serializers.ModelSerializer):
	cve_empresa = serializers.IntegerField(required=False)
	fecha_alta =serializers.DateTimeField(format='%d/%m/%Y',input_formats=['%d/%m/%Y'])

	def get_validation_exclusions(self, *args, **kwargs):
		exclusions = super(EmpresaSerializer, self).get_validation_exclusions(*args, **kwargs)
		return exclusions + ['cve_empresa']

	class Meta:
		model = Empresa
		fields = ('id','cve_empresa','razon_social','rfc','calle','numero','numero_int','colonia','cp','cdu_estado','cdu_giro',
				'cdu_municipio','telefono1','telefono2','cdu_giro','cdu_rubro','fecha_alta','latitud','longitud','user',)					
	

class PaginatedEmpresaSerializer(pagination.PaginationSerializer):
	class Meta:
		object_serializer_class = EmpresaSerializer