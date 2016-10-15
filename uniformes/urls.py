from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from uniformes import views

urlpatterns = patterns('uniformes.views',
 	 url(r'^uniforme/$',views.UniformeConDetallesLista.as_view(), name='uniforme_post_view'),
 	 url(r'^uniforme/personal/$',views.PersonalUniformeConDetalles.as_view(), name='personal_uniforme_view'),
	)