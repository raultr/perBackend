from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from uniformes_detalle import views

urlpatterns = patterns('uniformes_detalle.views',
 	 url(r'^uniformes_detalle/$',views.UniformeDetalleConDetallesLista.as_view(), name='uniforme_detalle_post_view'),
	)