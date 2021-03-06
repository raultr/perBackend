from django.core.files import File
import urllib
from django.db import models
from django.contrib.auth.models import User
from audit_log.models.managers import AuditLog
from catalogos_detalle.models import CatalogoDetalle
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError



class Empresa(models.Model):
	cve_empresa = models.IntegerField(unique=True)
	razon_social = models.CharField(max_length=150)
	rfc = models.CharField(max_length=13)
	calle = models.CharField(max_length=100)
	numero = models.CharField(max_length=10)
	numero_int =models.CharField(max_length=10,default='', blank=True)
	colonia = models.CharField(max_length=100)
	cp = models.CharField(max_length=10)
	cdu_estado =models.ForeignKey(CatalogoDetalle,to_field='cdu_catalogo',default='',related_name='empresa_cdu_estado',limit_choices_to={'catalogos': 14})
	cdu_municipio = models.ForeignKey(CatalogoDetalle,to_field='cdu_catalogo',default='',related_name='empresa_cdu_municipio',limit_choices_to={'catalogos': 15})
	telefono1 =models.CharField(max_length=10)
	telefono2 =models.CharField(max_length=10,default='', blank=True)
	cdu_giro = models.ForeignKey(CatalogoDetalle,to_field='cdu_catalogo',default='',related_name='empresa_cdu_giro',limit_choices_to={'catalogos': 18})
	cdu_rubro = models.ForeignKey(CatalogoDetalle,to_field='cdu_catalogo',default='',related_name='empresa_cdu_rubro',limit_choices_to={'catalogos': 19})
	fecha_alta =models.DateField(default = '1900-01-01')
	latitud = models.DecimalField(max_digits=12, decimal_places=7, default=-99.1696000)
	longitud = models.DecimalField(max_digits=12, decimal_places=7, default=19.5225000)
	user = models.ForeignKey(User,null=True)

	audit_log = AuditLog()
	
	def str(self):
		return self.razon_social

	def __unicode__(self):
		return '%s: %s' % (self.cve_empresa, self.razon_social)

	def pre_save(self, obj):
		if isinstance(self.request.user , User):   
			setattr(obj, 'user', self.request.user)
		else:
			setattr(obj, 'user', None)  