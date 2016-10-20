from django.conf.urls import patterns, url
from permisos import views

urlpatterns =[
 	url(r'^permiso_administrador/$', views.PermisoAdministrador.as_view()),
 	url(r'^permiso_administrador/rol/(?P<rol_buscado>[A-Za-z0-9\s]+)/$',views.PermisoRolBuscar.as_view(), name='permiso_rol_busqueda_view'),
	
]