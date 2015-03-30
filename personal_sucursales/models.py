import urllib
from django.db import models
from catalogos_detalle.models import CatalogoDetalle
from personal.models import Personal
from sucursales.models import Sucursal

class PersonalSucursal(models.Model):
	id_personal = models.ForeignKey(Personal,related_name='personalsucursal_id_personal')
	id_sucursal = models.ForeignKey(Sucursal,related_name='personalsucursal_id_sucursal')
	cdu_motivo =models.ForeignKey(CatalogoDetalle,to_field='cdu_catalogo',default='',related_name=' personalsucursal_cdu_motivo',limit_choices_to={'catalogos': 25})
	cdu_turno =models.ForeignKey(CatalogoDetalle,to_field='cdu_catalogo',default='',related_name=' personalsucursal_cdu_turno',limit_choices_to={'catalogos': 26})
	cdu_puesto =models.ForeignKey(CatalogoDetalle,to_field='cdu_catalogo',default='',related_name=' personalsucursal_cdu_puesto',limit_choices_to={'catalogos': 27})
	cdu_rango =models.ForeignKey(CatalogoDetalle,to_field='cdu_catalogo',default='',related_name=' personalsucursal_cdu_rango',limit_choices_to={'catalogos': 28})
	sueldo = models.DecimalField(max_digits=12, decimal_places=7, default=0.0)
	fecha_inicial = models.DateField(default = '1900-01-01')
	fecha_final = models.DateField(default = '1900-01-01')
	motivo = models.CharField(max_length=100)

	def str(self):
		return self.id_personal + " - " + self.id_sucursal 

	def activa(self):
		return self.fecha_final =="1900-01-01"

