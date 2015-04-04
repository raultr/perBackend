from rest_framework import serializers
from .models import PersonalSucursal
from sucursales.models import Sucursal
from catalogos_detalle.serializers import CatalogoSerializer
from sucursales.serializers import SucursalSerializer



class PersonalSucursalSerializer(serializers.ModelSerializer):
	id_sucursal = SucursalSerializer(read_only=True)
	cdu_motivo = CatalogoSerializer(read_only=True)
	cdu_turno = CatalogoSerializer(read_only=True)
	cdu_puesto = CatalogoSerializer(read_only=True)
	cdu_rango = CatalogoSerializer(read_only=True)
	
	#id_sucursal__nombre= serializers.PrimaryKeyRelatedField( queryset=Sucursal.objects.all(), source='id_sucursal')
	#sucursal_id = serializers.PrimaryKeyRelatedField( queryset=Personal.objects.all(), source='id_personal')

	class Meta:
		model = PersonalSucursal
		fields =('id','id_personal','id_sucursal','cdu_motivo','cdu_turno','cdu_puesto','cdu_rango','sueldo',
				'fecha_inicial','fecha_final','motivo',)