from django.contrib import admin

from .models import Permiso

class PermisoAdmin(admin.ModelAdmin):
	list_display =('id','rol','permisos')
	list_filter =('rol',)
	search_fields = ('permisos',) 
			
admin.site.register(Permiso,PermisoAdmin)