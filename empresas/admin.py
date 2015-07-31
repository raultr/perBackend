from django.contrib import admin

from .models import Empresa

class EmpresaAdmin(admin.ModelAdmin):
	list_display =('id','cve_empresa','razon_social','rfc','calle','numero','colonia','cp','cdu_estado','cdu_giro',
				'cdu_municipio','ciudad','telefono1','telefono2','cdu_giro','cdu_rubro','fecha_alta',)


	search_fields = ('id_empresa','razon_social','rfc') # Campos por los que se puede buscar, si son campos foraneos se usa campo__nomcampoforaneo
	list_filter =('cdu_giro','cdu_estado','cdu_municipio','cdu_rubro')
	list_editable = ('razon_social','rfc') # Hace el campo editable, (no debe ser el primer campo del list_display)
	raw_id_fields = ('cdu_estado',) # Para que me muestre solo el id y si queremos buscarlo por nombre nos pone una lupita
	
			
admin.site.register(Empresa,EmpresaAdmin)