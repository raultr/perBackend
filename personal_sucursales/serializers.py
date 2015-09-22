from rest_framework import serializers
from .models import PersonalSucursal
from sucursales.models import Sucursal
from personal.serializers import PersonalSerializer
from catalogos_detalle.models import CatalogoDetalle
from catalogos_detalle.serializers import CatalogoSerializer
from sucursales.serializers import SucursalSerializer



class PersonalSucursalSerializer(serializers.ModelSerializer):
	id_sucursal = SucursalSerializer(read_only=True, required=False)
	cdu_motivo = CatalogoSerializer(read_only=True, required=False)
	cdu_turno = CatalogoSerializer(read_only=True, required=False)
	cdu_puesto = CatalogoSerializer(read_only=True, required=False)
	cdu_rango = CatalogoSerializer(read_only=True, required=False)
	fecha_inicial =serializers.DateTimeField(format='%d/%m/%Y',input_formats=['%d/%m/%Y'])
	fecha_final =serializers.DateTimeField(format='%d/%m/%Y',input_formats=['%d/%m/%Y'])
	id_sucursalId = serializers.PrimaryKeyRelatedField(write_only=True,  source='id_sucursal')
	cdu_motivo_id = serializers.PrimaryKeyRelatedField(write_only=True,  source='cdu_motivo')
	cdu_turno_id = serializers.PrimaryKeyRelatedField(write_only=True,  source='cdu_turno')
	cdu_puesto_id = serializers.PrimaryKeyRelatedField(write_only=True,source='cdu_puesto')
	cdu_rango_id = serializers.PrimaryKeyRelatedField(write_only=True, source='cdu_rango')
	#id_sucursal__nombre= serializers.PrimaryKeyRelatedField( queryset=Sucursal.objects.all(), source='id_sucursal')
	#sucursal_id = serializers.PrimaryKeyRelatedField( queryset=Personal.objects.all(), source='id_personal')

	# def pre_save(self, obj):
	# 	if 'id_sucursalId' in self.request.DATA:
	# 		 custom_target = self.request.DATA['id_sucursalId']
	# 		 self.request.DATA['id_sucursalId'] = custom_target['id']

	class Meta:
		model = PersonalSucursal
		fields =('id','id_personal','id_sucursal','cdu_motivo','cdu_turno','cdu_puesto','cdu_rango','sueldo',
		 		'fecha_inicial','fecha_final','motivo','id_sucursalId','cdu_motivo_id','cdu_turno_id','cdu_puesto_id','cdu_rango_id','user',)

class PersonalSucursalSerializerSimple(serializers.ModelSerializer):
	fecha_inicial =serializers.DateTimeField(format='%d/%m/%Y',input_formats=['%d/%m/%Y'])
	fecha_final =serializers.DateTimeField(format='%d/%m/%Y',input_formats=['%d/%m/%Y'])
	class Meta:
		model = PersonalSucursal
		fields =('id','id_personal','id_sucursal','cdu_motivo','cdu_turno','cdu_puesto','cdu_rango','sueldo',
		 		'fecha_inicial','fecha_final','motivo','user')

class PersonalSucursalSerializerPersonal(serializers.ModelSerializer):
	id_personal =PersonalSerializer(read_only=True, required= False)
	class Meta:
		model = PersonalSucursal
		fields =('id','id_personal')