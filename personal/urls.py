from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from personal import views

urlpatterns = patterns('personal.views',
  	 #url(r'^personal/$', 'request_response_list'),
#	 url(r'^personal/(?P<id_matricula>[0-9]+)/$','request_response_detail', name='catalogo_detalle_view'),
#	 url(r'^personal/(?P<valor_buscado>[A-Za-z\s]+)/$','request_response_busqueda', name='catalogo_detalle_view'),
	 url(r'^personal/$',views.PersonalOperaciones.as_view(), name='catalogo_detalle_view_guardar'),
	 url(r'^personal/(?P<valor_buscado>[A-Za-z0-9\s]+)/$',views.PersonalBusqueda.as_view(), name='catalogo_detalle_view'),
	)