from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from incidencias import views

urlpatterns = patterns('incidencias.views',
	 url(r'^incidencias/personal/(?P<id_perso>[0-9]+)/$',views.IncidenciaOperaciones.as_view(), name='incidencia_view'),
	 url(r'^incidencias/personal/(?P<id_perso>[0-9]+)/fecha/(?P<fecha_incide>\d{2}-\d{2}-\d{4})/$',views.IncidenciaPersonalFecha.as_view(), name='incidencia_view')
	 ,)






#r'^(?P<month>\d{2})-(?P<day>\d{2})-(?P<year>\d{4})/$'