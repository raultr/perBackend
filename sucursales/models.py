from django.core.files import File
import urllib
from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from catalogos_detalle.models import CatalogoDetalle
from empresas.models import Empresa


class Sucursal(models.Model):
	cve_empresa = models.ForeignKey(Empresa, related_name='empresa_sucursal')
	cve_sucursal= models.IntegerField(unique=True)
	nombre  = models.CharField(max_length=150)
	calle = models.CharField(max_length=100)
	numero = models.CharField(max_length=10)
	colonia = models.CharField(max_length=100)
	cp = models.CharField(max_length=10)
	cdu_estado =models.ForeignKey(CatalogoDetalle,to_field='cdu_catalogo',default='',related_name='sucursal_cdu_estado',limit_choices_to={'catalogos': 14})
	cdu_municipio = models.ForeignKey(CatalogoDetalle,to_field='cdu_catalogo',default='',related_name='sucursal_cdu_municipio',limit_choices_to={'catalogos': 15})
	ciudad =models.CharField(max_length=100)
	telefono =models.CharField(max_length=10)
	cdu_estatus = models.ForeignKey(CatalogoDetalle,to_field='cdu_catalogo',default='',related_name='sucursal_cdu_estatus',limit_choices_to={'catalogos': 24})
	fecha_alta =models.DateField(default = '1900-01-01')
	fecha_baja =models.DateField(default = '1900-01-01')	
	latitud = models.DecimalField(max_digits=12, decimal_places=7, default=-99.1696000)
	longitud = models.DecimalField(max_digits=12, decimal_places=7, default=19.5225000)
	
	def str(self):
		return self.nombre