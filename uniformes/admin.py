from django.contrib import admin
from .models import Uniforme

class UniformeAdmin(admin.ModelAdmin):
	list_display =('id','id_personal','fecha','anio','periodo','observaciones', )
	search_fields = ('id_personal',) 
	list_filter =('anio','periodo',)

admin.site.register(Uniforme, UniformeAdmin)