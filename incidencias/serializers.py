from rest_framework import serializers
from .models import Incidencia
from personal.serializers import PersonalSerializer
from catalogos_detalle.serializers import CatalogoSerializer
from personal_sucursales.serializers import PersonalSucursalSerializerSimple

class IncidenciaSerializer(serializers.ModelSerializer):
	#cdu_concepto_incidencia = CatalogoSerializer(read_only=True, required=False)
	fecha =serializers.DateTimeField(format='%d/%m/%Y',input_formats=['%d/%m/%Y'])
	class Meta:
		model = Incidencia
		fields =('id','id_personal','cdu_concepto_incidencia','fecha','observaciones',)

class IncidenciaRelacionSerializer(serializers.ModelSerializer):
	id_personal__personalsucursal_id_personal= PersonalSucursalSerializerSimple(read_only=True, required= False)
 	cdu_concepto_incidencia = CatalogoSerializer(read_only=True, required=False)
	id_personal =PersonalSerializer(read_only=True, required= False)
	fecha =serializers.DateTimeField(format='%d/%m/%Y',input_formats=['%d/%m/%Y'])
	class Meta:
		model = Incidencia
		fields =('id','id_personal','cdu_concepto_incidencia','fecha','observaciones','id_personal__personalsucursal_id_personal',)