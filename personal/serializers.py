from rest_framework import serializers
from .models import Personal

class PersonalSerializer(serializers.ModelSerializer):
	class Meta:
		model = Personal

		fields =('matricula','paterno','materno','nombre','rfc','curp','cuip','fec_nacimiento',
			'cdu_estado_nac','cdu_municipio_nac','cdu_escolaridad','cdu_religion',
			 'cdu_seguridad_social','id_seguridad_social','portacion',)