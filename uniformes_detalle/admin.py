from django.contrib import admin
from .models import UniformeDetalle

class UniformeDetalleAdmin(admin.ModelAdmin):
	list_display =('id','uniforme','cdu_concepto_uniforme', )
	search_fields = ('uniforme',) 
	list_filter =('cdu_concepto_uniforme',)

admin.site.register(UniformeDetalle, UniformeDetalleAdmin)