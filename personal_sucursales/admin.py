from django.contrib import admin
from .models import PersonalSucursal

class PersonalSucursalAdmin(admin.ModelAdmin):
	list_display =('id','activa','id_personal','id_sucursal','cdu_motivo','cdu_turno','cdu_puesto','cdu_rango','sueldo',
				'fecha_inicial','fecha_final','motivo', )
	search_fields = ('id_personal__matricula','id_sucursal__cve_sucursal','id_sucursal__nombre',) # Campos por los que se puede buscar, si son campos foraneos se usa campo__nomcampoforaneo
	list_filter =('cdu_motivo','cdu_turno','cdu_puesto','cdu_rango',)
	list_editable = ('motivo',) # Hace el campo editable, (no debe ser el primer campo del list_display)
	
admin.site.register(PersonalSucursal,PersonalSucursalAdmin)

