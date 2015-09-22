from django.core.files import File
import urllib
from django.db import models
from django.contrib.auth.models import User
from audit_log.models.fields import LastUserField
from audit_log.models.managers import AuditLog
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from catalogos_detalle.models import CatalogoDetalle
from empresas.models import Empresa



class Sucursal(models.Model):
	cve_empresa = models.ForeignKey(Empresa, related_name='empresa_sucursal',on_delete = models.PROTECT)
	cve_sucursal= models.IntegerField(unique=True)
	nombre  = models.CharField(max_length=150)
	calle = models.CharField(max_length=100)
	numero = models.CharField(max_length=10)
	numero_int =models.CharField(max_length=10,default='', blank=True)
	colonia = models.CharField(max_length=100)
	cp = models.CharField(max_length=10)
	cdu_estado =models.ForeignKey(CatalogoDetalle,to_field='cdu_catalogo',default='',related_name='sucursal_cdu_estado',limit_choices_to={'catalogos': 14},on_delete = models.PROTECT)
	cdu_municipio = models.ForeignKey(CatalogoDetalle,to_field='cdu_catalogo',default='',related_name='sucursal_cdu_municipio',limit_choices_to={'catalogos': 15},on_delete = models.PROTECT)
	telefono =models.CharField(max_length=10)
	cdu_estatus = models.ForeignKey(CatalogoDetalle,to_field='cdu_catalogo',default='',related_name='sucursal_cdu_estatus',limit_choices_to={'catalogos': 24},on_delete = models.PROTECT)
	fecha_alta =models.DateField(default = '1900-01-01')
	fecha_baja =models.DateField(default = '1900-01-01')	
	latitud = models.DecimalField(max_digits=12, decimal_places=7, default=19.5225000)
	longitud = models.DecimalField(max_digits=12, decimal_places=7, default=-99.1696000)
	user = models.ForeignKey(User,null=True)

	audit_log = AuditLog()
	
	def str(self):
		return self.nombre

	def __unicode__(self):
		return '(%d) %s' % (self.cve_sucursal,self.nombre)