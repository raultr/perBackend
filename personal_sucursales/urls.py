from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from personal_sucursales import views

urlpatterns = patterns('personal_sucursales.views',
 	 url(r'^personal_sucursales/personal/(?P<id_perso>[0-9]+)/$',views.PersonalSucursalOperaciones.as_view(), name='personal_sucursales_view'),
 	 url(r'^personal_sucursales/personal/$',views.PersonalSucursalOperaciones.as_view(), name='personal_sucursales_view'),
	 url(r'^personal/(?P<id_perso>[0-9]+)/sucursal/activa/$',views.PersonalSucursalOperaciones.as_view(), name='catalogo_detalle_view_modificar'),
	)
