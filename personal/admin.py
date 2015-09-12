from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import fields,resources
from import_export.widgets import ForeignKeyWidget
from catalogos_detalle.models import CatalogoDetalle
from .models import Personal

class PersonalResource(resources.ModelResource):
	estado_nac = fields.Field(column_name='estado_nac', attribute='cdu_estado_nac', widget=ForeignKeyWidget(CatalogoDetalle, 'descripcion1')) 
	municipio_nac = fields.Field(column_name='municipio_nac', attribute='cdu_municipio_nac', widget=ForeignKeyWidget(CatalogoDetalle, 'descripcion1')) 
	genero = fields.Field(column_name='genero', attribute='cdu_genero', widget=ForeignKeyWidget(CatalogoDetalle, 'descripcion1')) 
	estado_civil = fields.Field(column_name='estado_civil', attribute='cdu_estado_civil', widget=ForeignKeyWidget(CatalogoDetalle, 'descripcion1')) 
	escolaridad = fields.Field(column_name='escolaridad', attribute='cdu_escolaridad', widget=ForeignKeyWidget(CatalogoDetalle, 'descripcion1')) 
	seguridad_social = fields.Field(column_name='seguridad_social', attribute='cdu_seguridad_social', widget=ForeignKeyWidget(CatalogoDetalle, 'descripcion1')) 
	tipo_alta = fields.Field(column_name='tipo_alta', attribute='cdu_tipo_alta', widget=ForeignKeyWidget(CatalogoDetalle, 'descripcion1')) 
	tipo_empleado = fields.Field(column_name='tipo_empleado', attribute='cdu_tipo_empleado', widget=ForeignKeyWidget(CatalogoDetalle, 'descripcion1')) 
	estado_dom = fields.Field(column_name='estado_dom', attribute='cdu_estado_dom', widget=ForeignKeyWidget(CatalogoDetalle, 'descripcion1')) 
	municipio_dom = fields.Field(column_name='municipio_dom', attribute='cdu_municipio_dom', widget=ForeignKeyWidget(CatalogoDetalle, 'descripcion1')) 
	
	class Meta: 
		model = Personal
		fields = ('id','matricula','paterno','materno','nombre','nombre_completo','rfc','curp','cuip','fec_nacimiento',
					'estado_nac','municipio_nac','genero','estado_civil','escolaridad','seguridad_social',
					'id_seguridad_social','telefono','portacion','tipo_alta','fec_alta','condicionada','condiciones_alta','tipo_empleado','calle_dom',
					'numero_dom','numero_int_dom','colonia_dom','cp_dom','estado_dom','municipio_dom',)
		export_order = ('id','matricula','paterno','materno','nombre','rfc','curp','cuip','fec_nacimiento',
					'estado_nac','municipio_nac','genero','estado_civil','escolaridad','seguridad_social',
					'id_seguridad_social','telefono','portacion','tipo_alta','fec_alta','condicionada','condiciones_alta','tipo_empleado','calle_dom',
					'numero_dom','numero_int_dom','colonia_dom','cp_dom','estado_dom','municipio_dom',)

class PersonalAdmin2(ImportExportModelAdmin):
	resource_class = PersonalResource
					

#class import_export.fields.Field(attribute=None, column_name=None, widget=None, readonly=False)
class PersonalAdmin(ImportExportModelAdmin):
	#cdu_estado_nac = fields.Field(column_name='cdu_estado_nac', attribute='descripcion1', widget=ForeignKeyWidget('cdu_estado_nac', 'descripcion1')) 
	estado_nac = fields.Field(column_name='cdu_estado_nac', attribute='descripcion1',      widget=ForeignKeyWidget(CatalogoDetalle, 'descripcion1'))
	#class Meta: 
	#	fields = ('author')
	list_display =('id','matricula','paterno','materno','nombre','nombre_completo','rfc','curp','cuip','fec_nacimiento',
					'cdu_estado_nac','cdu_municipio_nac','cdu_genero','cdu_estado_civil','cdu_escolaridad','cdu_seguridad_social',
					'id_seguridad_social','telefono','portacion','cdu_tipo_alta','fec_alta','condicionada','condiciones_alta','cdu_tipo_empleado','calle_dom',
					'numero_dom','numero_int_dom','colonia_dom','cp_dom','cdu_estado_dom','cdu_municipio_dom',)
					
	search_fields = ('matricula','paterno','materno','nombre') # Campos por los que se puede buscar, si son campos foraneos se usa campo__nomcampoforaneo
	list_filter =('portacion',)
	list_editable = ('paterno','materno','nombre',) # Hace el campo editable, (no debe ser el primer campo del list_display)
	#raw_id_fields = ('catalogos',) # Para que me muestre solo el id y si queremos buscarlo por nombre nos pone una lupita

	# def estado_nac(self,obj):
	# 	return obj.cdu_estado_nac.descripcion1
	
admin.site.register(Personal,PersonalAdmin2)