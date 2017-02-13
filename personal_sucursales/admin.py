from django.contrib import admin
from .models import PersonalSucursal
from import_export.admin import ImportExportModelAdmin,ExportMixin,ExportActionModelAdmin
from import_export import fields,resources
from import_export.widgets import ForeignKeyWidget
from catalogos_detalle.models import CatalogoDetalle
from personal.models import Personal
from sucursales.models import Sucursal

class PersonalSucursalResource(resources.ModelResource):
	paterno = fields.Field(column_name='paterno', attribute='id_personal', widget=ForeignKeyWidget(Personal, 'paterno')) 
	materno = fields.Field(column_name='materno', attribute='id_personal', widget=ForeignKeyWidget(Personal, 'materno')) 
	nombre = fields.Field(column_name='nombre', attribute='id_personal', widget=ForeignKeyWidget(Personal, 'nombre')) 
	
	sucursal = fields.Field(column_name='sucursal', attribute='id_sucursal', widget=ForeignKeyWidget(Sucursal, 'nombre')) 
	motivo = fields.Field(column_name='motivo', attribute='cdu_motivo', widget=ForeignKeyWidget(CatalogoDetalle, 'descripcion1')) 
	turno = fields.Field(column_name='turno', attribute='cdu_turno', widget=ForeignKeyWidget(CatalogoDetalle, 'descripcion1')) 
	puesto = fields.Field(column_name='puesto', attribute='cdu_puesto', widget=ForeignKeyWidget(CatalogoDetalle, 'descripcion1')) 
	rango = fields.Field(column_name='rango', attribute='cdu_rango', widget=ForeignKeyWidget(CatalogoDetalle, 'descripcion1')) 
	
	class Meta: 
		model = PersonalSucursal
		fields = ('id','id_personal','nombre','paterno','materno','id_sucursal','sucursal','turno','puesto','rango','sueldo',
				'fecha_inicial','fecha_final','motivo', )
		export_order = ('id','id_personal','nombre','paterno','materno','id_sucursal','sucursal','turno','puesto','rango','sueldo',
				'fecha_inicial','fecha_final','motivo', )


class PersonalSucursalAdmin2(ImportExportModelAdmin):
	resource_class = PersonalSucursalResource
	list_display =('id','activa','id_personal','id_sucursal','cdu_motivo','cdu_turno','cdu_puesto','cdu_rango','sueldo',
				'fecha_inicial','fecha_final','motivo', )
	search_fields = ('id_personal__matricula','id_sucursal__cve_sucursal','id_sucursal__nombre',) # Campos por los que se puede buscar, si son campos foraneos se usa campo__nomcampoforaneo
	list_filter =('cdu_motivo','cdu_turno','cdu_puesto','cdu_rango',)


class PersonalSucursalAdmin(admin.ModelAdmin):
	list_display =('id','activa','id_personal','id_sucursal','cdu_motivo','cdu_turno','cdu_puesto','cdu_rango','sueldo',
				'fecha_inicial','fecha_final','motivo', )
	search_fields = ('id_personal__matricula','id_sucursal__cve_sucursal','id_sucursal__nombre',) # Campos por los que se puede buscar, si son campos foraneos se usa campo__nomcampoforaneo
	list_filter =('cdu_motivo','cdu_turno','cdu_puesto','cdu_rango',)
	list_editable = ('motivo',) # Hace el campo editable, (no debe ser el primer campo del list_display)
	
admin.site.register(PersonalSucursal,PersonalSucursalAdmin2)