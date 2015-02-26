from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PersoRegBackEnd.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('catalogos.urls')),
    url(r'^', include('catalogos_detalle.urls')),
    url(r'^', include('personal.urls')),
    url(r'^', include('empresas.urls')),
    url(r'^', include('sucursales.urls')),
    url(r'^', include('subirf.urls')),
)


if settings.DEBUG:
	urlpatterns += patterns('',
	url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root': settings.MEDIA_ROOT,}),)
