# -*- encoding: utf-8 -*-
from django.core.exceptions import ValidationError
import urllib
from django.db import transaction
from django.db import models
from catalogos_detalle.models import CatalogoDetalle
from personal.models import Personal
from sucursales.models import Sucursal

class PersonalSucursal(models.Model):
	id_personal = models.ForeignKey(Personal,related_name='personalsucursal_id_personal', on_delete=models.PROTECT)
	id_sucursal = models.ForeignKey(Sucursal,related_name='personalsucursal_id_sucursal', on_delete=models.PROTECT)
	cdu_motivo =models.ForeignKey(CatalogoDetalle,to_field='cdu_catalogo',default='',related_name=' personalsucursal_cdu_motivo',limit_choices_to={'catalogos': 25}, on_delete=models.PROTECT)
	cdu_turno =models.ForeignKey(CatalogoDetalle,to_field='cdu_catalogo',default='',related_name=' personalsucursal_cdu_turno',limit_choices_to={'catalogos': 26}, on_delete=models.PROTECT)
	cdu_puesto =models.ForeignKey(CatalogoDetalle,to_field='cdu_catalogo',default='',related_name=' personalsucursal_cdu_puesto',limit_choices_to={'catalogos': 27}, on_delete=models.PROTECT)
	cdu_rango =models.ForeignKey(CatalogoDetalle,to_field='cdu_catalogo',default='',related_name=' personalsucursal_cdu_rango',limit_choices_to={'catalogos': 28}, on_delete=models.PROTECT)
	sueldo = models.DecimalField(max_digits=12, decimal_places=7, default=0.0)
	fecha_inicial = models.DateField(default = '1900-01-01')
	fecha_final = models.DateField(default = '1900-01-01')
	motivo = models.CharField(max_length=100,blank=True)

	def str(self):
		return self.id_personal + " - " + self.id_sucursal 

	def activa(self):
		return self.fecha_final =="1900-01-01"

	@transaction.atomic
	def save(self, *args, **kwargs):
			self.validarFechas()
			#falta validar que el elemento este activo y la sucursal este activa
			#Actualizamo la asignacion anterior	
			PersonalSucursal.objects.filter(id_personal=self.id_personal, fecha_final="1900-01-01",fecha_inicial__lt=self.fecha_inicial).update(fecha_final=self.fecha_inicial)
			super(PersonalSucursal, self).save(*args, **kwargs)

	@transaction.atomic
	def delete(self, *args, **kwargs):
		self.validarEliminacion()
		# Al eliminar una asignacion, a la asignacion anterior es la activa y se le asigna fec_inicial='01/01/1900' 
		anterior = PersonalSucursal.objects.filter(id_personal=self.id_personal).exclude(id=self.id).order_by('id').reverse()[0]
		PersonalSucursal.objects.filter(id = anterior.id).update(fecha_final="1900-01-01")
		super(PersonalSucursal, self).delete(*args, **kwargs)

	def validarEliminacion(self):
		# Si solo hay una asignacion, no es posible eliminarla
		cantidad = PersonalSucursal.objects.filter(id_personal=self.id_personal).count()
		if(cantidad==1):
			raise ValidationError('El elemento solo tiene una asignacion y no es posible eliminarla')
		if (self.fecha_final.strftime("%d-%m-%Y") != "01-01-1900"):
			raise ValidationError('Solo se pueden elimnar asignaciones activas')
		return True

	def validarFechas(self):
		#import ipdb; ipdb.set_trace()
		#Revisamos que no existan asignacion con una fecha mayor a la que queremos.
		fecMayor=PersonalSucursal.objects.filter(id_personal=self.id_personal, fecha_inicial__gte= self.fecha_inicial).count()
		if fecMayor>0:
			raise ValidationError('Ya existe una asignación mayor o igual a ' + self.fecha_inicial.strftime('%d/%m/%Y'))

		#Revisamos que la asignacion no sea con los mismos datos que la actual
		asignacionIgual=PersonalSucursal.objects.filter(id_personal=self.id_personal, fecha_final="1900-01-01",id_sucursal=self.id_sucursal,
			cdu_motivo=self.cdu_motivo,cdu_turno=self.cdu_turno,cdu_puesto=self.cdu_puesto,cdu_rango=self.cdu_rango,sueldo=self.sueldo).count()
		if asignacionIgual>0:
			raise ValidationError('La asignación contiene los mismos datos que la actual')