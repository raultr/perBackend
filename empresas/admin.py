from django.contrib import admin

from .models import Empresa

class EmpresaAdmin(admin.ModelAdmin):
	list_display =('id_empresa','razon_social','rfc','cdu_giro','cdu_rubro',)
	search_fields = ('id_empresa','razon_social',) # Campos por los que se puede buscar, si son campos foraneos se usa campo__nomcampoforaneo
	list_filter =('cdu_giro','cdu_estado',)
	list_editable = ('razon_social',) # Hace el campo editable, (no debe ser el primer campo del list_display)
	raw_id_fields = ('cdu_estado',) # Para que me muestre solo el id y si queremos buscarlo por nombre nos pone una lupita
	
			
admin.site.register(Empresa,EmpresaAdmin)