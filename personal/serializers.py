from rest_framework import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Personal
from rest_framework.response import Response
from rest_framework import pagination

class ImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Personal
		fields =('id','imagen',)

class PersonalSerializer(serializers.ModelSerializer):
	matricula = serializers.IntegerField(required=False)
	fec_nacimiento = serializers.DateTimeField(format='%d/%m/%Y',input_formats=['%d/%m/%Y'])
	fec_alta =serializers.DateTimeField(format='%d/%m/%Y',input_formats=['%d/%m/%Y'])

	def get_validation_exclusions(self, *args, **kwargs):
		exclusions = super(PersonalSerializer, self).get_validation_exclusions(*args, **kwargs)
		#import ipdb; ipdb.set_trace()
		return exclusions + ['matricula']

	class Meta:
		model = Personal
	
		fields =('id','paterno','matricula','materno','nombre','rfc','curp','cuip','fec_nacimiento',
			'cdu_estado_nac','cdu_municipio_nac','cdu_genero','cdu_estado_civil','cdu_escolaridad',
			 'cdu_seguridad_social','id_seguridad_social','portacion','cdu_tipo_alta','fec_alta','condicionada','condiciones_alta','cdu_tipo_empleado','calle_dom',
					'numero_dom','colonia_dom','cp_dom','cdu_estado_dom','cdu_municipio_dom','imagen')
		read_only_fields =('imagen',)

		#read_only_fields = ('matricula',)django "Datetime has wrong format. Use one of these formats instead: YYYY-MM-DDThh:mm[:ss[.uuuuuu]][+HH:MM|-HH:MM|Z]"

class PaginatedPersonalSerializer(pagination.PaginationSerializer):
	class Meta:
		object_serializer_class = PersonalSerializer