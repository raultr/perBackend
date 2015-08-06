# -*- encoding: utf-8 -*-
from django.core.exceptions import ValidationError
import urllib
from django.db import transaction
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
	motivo = models.CharField(max_length=100,blank=True)

	def str(self):
		return self.id_personal + " - " + self.id_sucursal 

	def activa(self):
		return self.fecha_final =="1900-01-01"

	#@transaction.atomic
	def save(self, *args, **kwargs):
			self.validarFechas()
			#falta validar que el elemento este activo y la sucursal este activa
			#Actualizamo la asignacion anterior	
			PersonalSucursal.objects.filter(id_personal=self.id_personal, fecha_final="1900-01-01",fecha_inicial__lt=self.fecha_inicial).update(fecha_final=self.fecha_inicial)
			super(PersonalSucursal, self).save(*args, **kwargs)

	def validarFechas(self):
		#import ipdb; ipdb.set_trace()
		#Revisamos que no existan asignacion con una fecha mayor a la que queremos.
		fecMayor=PersonalSucursal.objects.filter(id_personal=self.id_personal, fecha_final="1900-01-01",fecha_inicial__gte= self.fecha_inicial).count()
		if fecMayor>0:
			raise ValidationError('La fecha de la asignación actual es mayor a la nueva fecha')

		#Revisamos que la asignacion no sea con los mismos datos que la actual
		asignacionIgual=PersonalSucursal.objects.filter(id_personal=self.id_personal, fecha_final="1900-01-01",id_sucursal=self.id_sucursal,
			cdu_motivo=self.cdu_motivo,cdu_turno=self.cdu_turno,cdu_puesto=self.cdu_puesto,cdu_rango=self.cdu_rango,sueldo=self.sueldo).count()
		if asignacionIgual>0:
			raise ValidationError('La asignación contiene los mismos datos que la actual')