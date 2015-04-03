from rest_framework import serializers
from .models import PersonalSucursal
from personal.models import Personal
from personal.serializers import PersonalSerializer


class PersonalSucursalSerializer(serializers.ModelSerializer):
	id_personal = PersonalSerializer(read_only=True)
	personal_id = serializers.PrimaryKeyRelatedField( queryset=Personal.objects.all(), source='id_personal')

	class Meta:
		model = PersonalSucursal
		fields =('id','id_personal','id_sucursal','cdu_motivo','cdu_turno','cdu_puesto','cdu_rango','sueldo',
				'fecha_inicial','fecha_final','motivo','personal_id',)
		#depth = 1