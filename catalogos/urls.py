from django.conf.urls import patterns, url
	
urlpatterns = patterns('catalogos.views',
	 url(r'^catalogos/$', 'request_response_list'),
	 url(r'^catalogos/editables/$', 'request_response_list_editables'),
	  url(r'^catalogos/(?P<pk>[0-9]+)/$', 'request_response_list2'),
     #url(r'^request_response/(?P<pk>[0-9]+)/$', 'request_response_detail'),
	)