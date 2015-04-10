from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from sucursales import views

urlpatterns = patterns('sucursales.views',
 	 url(r'^sucursal/(?P<pk>[0-9]+)/$',views.SucursalOperaciones.as_view(), name='sucursal_detalle_view'),
	 url(r'^sucursal/$',views.SucursalOperaciones.as_view(), name='sucursal_post_view'),
	 url(r'^sucursal/buscar/(?P<valor_buscado>[A-Za-z0-9\s]+)/$',views.SucursalBusqueda.as_view(), name='sucursal_busqueda_view'),
	 url(r'^empresa/(?P<id_empresa>[0-9]+)/sucursales/$',views.SucursalesEmpresa.as_view(), name='sucursales_empresa_view'),
	)

