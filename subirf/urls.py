from django.conf.urls import patterns, include, url
from .views import ImageView

urlpatterns = patterns('subirf.views',
	 url(r'^subirf/$', ImageView.as_view(), name='image'),
     #url(r'^request_response/(?P<pk>[0-9]+)/$', 'request_response_detail'),
	)