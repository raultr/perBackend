from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from personal_sucursales import views

urlpatterns = patterns('personal_sucursales.views',
	 url(r'^personal_sucursales/menu/$',views.PersonalSucusalMenu.as_view(), name='personal_sucursal_menu_view'),
 	 url(r'^personal_sucursales/personal/(?P<id_perso>[0-9]+)/$',views.PersonalSucursalOperaciones.as_view(), name='personal_sucursales_view'),
 	 url(r'^personal_sucursales/personal/$',views.PersonalSucursalOperaciones.as_view(), name='personal_sucursales_view'),
	 url(r'^personal/(?P<id_perso>[0-9]+)/sucursal/activa/$',views.PersonalSucursalConsultas.as_view(), name='personal_sucursales_consulta'), 
	 url(r'^sucursal/(?P<id_sucursal>[0-9]+)/personal/activo/$',views.PersonalSucursalConsultas.as_view(), name='personal_sucursales_consulta'), 
 	 #url(r'^personal_sucursales/$',views.PersonalSucursalView.as_view({'get': 'list',    'post': 'create'}), name='personal_sucursales_view'),
 	 url(r'^personal_sucursales/asignacion/(?P<pk>[0-9]+)/$',views.PersonalSucursalOperaciones.as_view(), name='personal_sucursales_view'),
	 url(r'^personal_sucursales/activos/empresa/(?P<id_empresa>[0-9,]+)/$',views.PersonalSucursalReportes.as_view(), name='personal_sucursales_reporte'), 
	 url(r'^personal_sucursales/(?P<id_perso>[0-9]+)/fecha/(?P<fecha_asignacion>\d{1,2}-\d{1,2}-\d{4})/$',views.PersonalSucursalFecha.as_view(), name='personal_sucursalfecha_view'),
 	 url(r'^personal_sucursales/$',views.PersonalSucursalOperaciones.as_view(), name='personal_sucursales_view'),)

