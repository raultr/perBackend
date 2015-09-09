from django.contrib import admin

from .models import Sucursal

class SucursalAdmin(admin.ModelAdmin):
	list_display =('id', 'cve_empresa','cve_sucursal','nombre','calle','numero','numero_int','colonia','cp',	'cdu_estado','cdu_municipio',
	               'telefono',	'cdu_estatus', 'fecha_alta','fecha_baja','latitud','longitud', )



	search_fields = ('cve_empresa','cve_sucursal','nombre') # Campos por los que se puede buscar, si son campos foraneos se usa campo__nomcampoforaneo
	list_filter =('cdu_estado','cdu_municipio','cdu_estatus')
	list_editable = ('nombre',) # Hace el campo editable, (no debe ser el primer campo del list_display)
	
			
admin.site.register(Sucursal,SucursalAdmin)