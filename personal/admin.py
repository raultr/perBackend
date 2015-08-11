from django.contrib import admin

from .models import Personal

class PersonalAdmin(admin.ModelAdmin):
	list_display =('id','matricula','paterno','materno','nombre','nombre_completo','rfc','curp','cuip','fec_nacimiento',
					'cdu_estado_nac','cdu_municipio_nac','cdu_estado_civil','cdu_escolaridad','cdu_seguridad_social',
					'id_seguridad_social','portacion','cdu_tipo_alta','fec_alta','condicionada','condiciones_alta','cdu_tipo_empleado','calle_dom',
					'numero_dom','colonia_dom','cp_dom','cdu_estado_dom','cdu_municipio_dom',)
					
	search_fields = ('matricula','paterno','materno','nombre') # Campos por los que se puede buscar, si son campos foraneos se usa campo__nomcampoforaneo
	list_filter =('portacion',)
	list_editable = ('paterno','materno','nombre','cdu_municipio_nac',) # Hace el campo editable, (no debe ser el primer campo del list_display)
	#raw_id_fields = ('catalogos',) # Para que me muestre solo el id y si queremos buscarlo por nombre nos pone una lupita
	
			
admin.site.register(Personal,PersonalAdmin)