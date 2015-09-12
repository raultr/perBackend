from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import fields,resources
from import_export.widgets import ForeignKeyWidget
from catalogos_detalle.models import CatalogoDetalle
from .models import Empresa

class EmpresaResource(resources.ModelResource):
	estado = fields.Field(column_name='estado', attribute='cdu_estado', widget=ForeignKeyWidget(CatalogoDetalle, 'descripcion1')) 
	municipio = fields.Field(column_name='municipio', attribute='cdu_municipio', widget=ForeignKeyWidget(CatalogoDetalle, 'descripcion1')) 
	giro = fields.Field(column_name='giro', attribute='cdu_giro', widget=ForeignKeyWidget(CatalogoDetalle, 'descripcion1')) 
	rubro = fields.Field(column_name='rubro', attribute='cdu_rubro', widget=ForeignKeyWidget(CatalogoDetalle, 'descripcion1')) 
	
	class Meta: 
		model = Empresa
		fields = ('id','cve_empresa','razon_social','rfc','calle','numero','numero_int','colonia','cp','estado','giro',
				'municipio','telefono1','telefono2','rubro','fecha_alta',)
		
		export_order = ('id','cve_empresa','razon_social','rfc','calle','numero','numero_int','colonia','cp','estado','giro',
				'municipio','telefono1','telefono2','rubro','fecha_alta',)

class EmpresaAdmin2(ImportExportModelAdmin):
	resource_class = EmpresaResource
	
	list_display =('id','cve_empresa','razon_social','rfc','calle','numero','numero_int','colonia','cp','cdu_estado','cdu_giro',
				'cdu_municipio','telefono1','telefono2','cdu_rubro','fecha_alta',)
	search_fields = ('id_empresa','razon_social','rfc') # Campos por los que se puede buscar, si son campos foraneos se usa campo__nomcampoforaneo
	list_filter =('cdu_giro','cdu_estado','cdu_municipio','cdu_rubro')

					
class EmpresaAdmin(ImportExportModelAdmin):
	list_display =('id','cve_empresa','razon_social','rfc','calle','numero','numero_int','colonia','cp','cdu_estado','cdu_giro',
				'cdu_municipio','telefono1','telefono2','cdu_rubro','fecha_alta',)


	search_fields = ('id_empresa','razon_social','rfc') # Campos por los que se puede buscar, si son campos foraneos se usa campo__nomcampoforaneo
	list_filter =('cdu_giro','cdu_estado','cdu_municipio','cdu_rubro')
	list_editable = ('razon_social','rfc') # Hace el campo editable, (no debe ser el primer campo del list_display)
	raw_id_fields = ('cdu_estado',) # Para que me muestre solo el id y si queremos buscarlo por nombre nos pone una lupita

admin.site.register(Empresa,EmpresaAdmin2)