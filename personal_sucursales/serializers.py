from rest_framework import serializers
from .models import PersonalSucursal


class PersonalSucursalSerializer(serializers.ModelSerializer):

	class Meta:
		model = PersonalSucursal
		fields =('id','id_personal','id_sucursal','cdu_motivo','cdu_turno','cdu_puesto','cdu_rango','sueldo',
				'fecha_inicial','fecha_final','motivo', )