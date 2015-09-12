from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import fields,resources
from import_export.widgets import ForeignKeyWidget
from catalogos_detalle.models import CatalogoDetalle
from empresas.models import  Empresa
from .models import Sucursal

class SucursalResource(resources.ModelResource):
	estado = fields.Field(column_name='estado', attribute='cdu_estado', widget=ForeignKeyWidget(CatalogoDetalle, 'descripcion1')) 
	municipio = fields.Field(column_name='municipio', attribute='cdu_municipio', widget=ForeignKeyWidget(CatalogoDetalle, 'descripcion1')) 
	estatus = fields.Field(column_name='estatus', attribute='cdu_estatus', widget=ForeignKeyWidget(CatalogoDetalle, 'descripcion1')) 
	empresa = fields.Field(column_name='empresa', attribute='cve_empresa', widget=ForeignKeyWidget(Empresa, 'razon_social')) 
	class Meta: 
		model = Sucursal
		fields = ('id', 'cve_empresa','empresa','cve_sucursal','nombre','calle','numero','numero_int','colonia','cp','estado','municipio',
				   'telefono',	'estatus', 'fecha_alta','fecha_baja','latitud','longitud', )

		export_order = ('id', 'cve_empresa','empresa','cve_sucursal','nombre','calle','numero','numero_int','colonia','cp','estado','municipio',
				   'telefono',	'estatus', 'fecha_alta','fecha_baja','latitud','longitud', )

class SucursalAdmin2(ImportExportModelAdmin):
	resource_class = SucursalResource
	list_display =('id', 'cve_empresa','cve_sucursal','nombre','calle','numero','numero_int','colonia','cp','cdu_estado','cdu_municipio',
				   'telefono',	'cdu_estatus', 'fecha_alta','fecha_baja','latitud','longitud', )

	search_fields = ('cve_empresa','cve_sucursal','nombre') # Campos por los que se puede buscar, si son campos foraneos se usa campo__nomcampoforaneo
	list_filter =('cdu_estado','cdu_municipio','cdu_estatus')
					

class SucursalAdmin(ImportExportModelAdmin):
	list_display =('id', 'cve_empresa','cve_sucursal','nombre','calle','numero','numero_int','colonia','cp','cdu_estado','cdu_municipio',
				   'telefono',	'cdu_estatus', 'fecha_alta','fecha_baja','latitud','longitud', )



	search_fields = ('cve_empresa','cve_sucursal','nombre') # Campos por los que se puede buscar, si son campos foraneos se usa campo__nomcampoforaneo
	list_filter =('cdu_estado','cdu_municipio','cdu_estatus')
	list_editable = ('nombre',) # Hace el campo editable, (no debe ser el primer campo del list_display)
	

admin.site.register(Sucursal,SucursalAdmin2)