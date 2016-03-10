
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from incidencias import views

urlpatterns = patterns('incidencias.views',
	 url(r'^incidencias/$',views.IncidenciaNueva.as_view(), name='incidencias_post_view'),
 	 url(r'^incidencias/(?P<pk>[0-9]+)/$',views.IncidenciaModificacion.as_view(), name='incidencias_post_view'),
 	 url(r'^incidencias/personal/(?P<id_perso>[0-9]+)/fecha/(?P<fecha_incide>\d{1,2}-\d{1,2}-\d{4})/$',views.IncidenciaPersonalFecha.as_view(), name='incidencia_view')
	 )