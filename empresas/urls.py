from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from empresas import views

urlpatterns = patterns('empresas.views',
 	 url(r'^empresa/(?P<pk>[0-9]+)/$',views.EmpresaOperaciones.as_view(), name='empresa_detalle_view'),
	 url(r'^empresa/$',views.EmpresaOperaciones.as_view(), name='empresa_post_view'),
	 url(r'^empresa/buscar/(?P<valor_buscado>[A-Za-z0-9\s]+)/$',views.EmpresaBusqueda.as_view(), name='empresa_busqueda_view'),
	 #url(r'^empresa/(?P<pk>[0-9]+)/sucursales/$',views.EmpresaReportes.as_view(), name='empresa_get_reporte'),
	)
