import urllib
from django.db import models


class Permiso(models.Model):
	rol = models.CharField(max_length=20,unique=True)
	permisos = models.CharField(max_length=200)
	
	def str(self):
		return self.rol

	def __unicode__(self):
		return '%s' % (self.rol)