from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from PersoRegBackEnd.views import AuthView,TestView,TacView
from rest_framework.authtoken import views


urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'PersoRegBackEnd.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	url(r'^admin/', include(admin.site.urls)),
	url(r'^auth/', AuthView.as_view(), name='auth-view'),
	url(r'^test/', TestView.as_view(), name='auth-view2'),
	url(r'^api-token-auth/', views.obtain_auth_token),
	url(r'^prueba_autenticacion/', TacView.as_view()),
	
	url(r'^', include('catalogos.urls')),
	url(r'^', include('catalogos_detalle.urls')),
	url(r'^', include('personal.urls')),
	url(r'^', include('empresas.urls')),
	url(r'^', include('sucursales.urls')),
	url(r'^', include('personal_sucursales.urls')),
	url(r'^', include('incidencias.urls')),
	url(r'^', include('subirf.urls')),
)
urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
	import debug_toolbar
	urlpatterns += patterns('',
	url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.MEDIA_ROOT,}),)
	urlpatterns += patterns('', url(r'^__debug__/', include(debug_toolbar.urls)),)