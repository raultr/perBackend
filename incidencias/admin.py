from django.contrib import admin
from .models import Incidencia
from personal.models import Personal

class IncidenciaInLine(admin.StackedInline): # No permite editar el catalogo_detalles en la misma pantalla de catalogos
	model = Personal #Para poder editar los detalles de un catalogo
	extra = 1 # Solo un registro adicional para agregar


class IncidenciaAdmin(admin.ModelAdmin):
	list_display =('id','cubre','id_personal','cdu_concepto_incidencia','fecha','observaciones', )
	search_fields = ('id_personal__matricula','id_sucursal__nombre',) # Campos por los que se puede buscar, si son campos foraneos se usa campo__nomcampoforaneo
	list_filter =('cdu_concepto_incidencia',)

admin.site.register(Incidencia, IncidenciaAdmin)