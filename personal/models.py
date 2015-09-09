from django.core.files import File
import urllib
from django.db import models
from catalogos_detalle.models import CatalogoDetalle
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(u'%s is not an even number' % value)

class Personal(models.Model):
	matricula = models.IntegerField(unique=True)
	paterno = models.CharField(max_length=20)
	materno = models.CharField(max_length=20)
	nombre = models.CharField(max_length=20)
	rfc = models.CharField(max_length=13)
	curp = models.CharField(max_length=18)
	cuip = models.CharField(max_length=30, blank=True)
	fec_nacimiento =models.DateField(default = '1900-01-01')
	cdu_estado_nac = models.ForeignKey(CatalogoDetalle,to_field='cdu_catalogo',default='',related_name='pesonal_cdu_estado_nac',limit_choices_to={'catalogos': 14},validators=[RegexValidator(regex='(?=^.{7,7}$)(^014)([0-9]{4})', message='El catalogo debe empezar con 14 y su longitud de 7', code='nomatch')])						
	cdu_municipio_nac =models.ForeignKey(CatalogoDetalle,to_field='cdu_catalogo',default='',related_name='pesonal_cdu_municipio_nac',limit_choices_to={'catalogos': 15})
	cdu_estado_civil =models.ForeignKey(CatalogoDetalle,to_field='cdu_catalogo',default='0010000',related_name='pesonal_cdu_estado_civil',limit_choices_to={'catalogos': 1})
	cdu_genero =models.ForeignKey(CatalogoDetalle,to_field='cdu_catalogo',default='0030001',related_name='pesonal_cdu_genero',limit_choices_to={'catalogos': 3})
	cdu_escolaridad =models.ForeignKey(CatalogoDetalle,to_field='cdu_catalogo',default='',related_name='pesonal_cdu_escolaridad',limit_choices_to={'catalogos': 2})
	cdu_seguridad_social = models.ForeignKey(CatalogoDetalle,to_field='cdu_catalogo',default='',related_name='pesonal_cdu_seguridad_social',limit_choices_to={'catalogos': 17})
	id_seguridad_social =models.CharField(max_length=20, blank=True)
	telefono = models.CharField(max_length=50, blank=True, default='')
	portacion = models.BooleanField(default=False)
	cdu_tipo_alta =models.ForeignKey(CatalogoDetalle,to_field='cdu_catalogo',default='0200000',related_name='pesonal_cdu_tipo_alta',limit_choices_to={'catalogos': 20})
	fec_alta=models.DateField(default = '1900-01-01')
	condicionada = models.BooleanField(default=False)
	condiciones_alta =models.CharField(max_length=150,default='', blank=True)
	cdu_tipo_empleado =models.ForeignKey(CatalogoDetalle,to_field='cdu_catalogo',default='0210000',related_name='pesonal_tipo_empleado',limit_choices_to={'catalogos': 21})
	calle_dom = models.CharField(max_length=100,default='')
	numero_dom = models.CharField(max_length=10,default='')
	numero_int_dom =models.CharField(max_length=10,default='',blank=True)
	colonia_dom = models.CharField(max_length=100,default='')
	cp_dom = models.CharField(max_length=10,default='')
	cdu_estado_dom =models.ForeignKey(CatalogoDetalle,to_field='cdu_catalogo',default='0140000',related_name='pesonal_cdu_estado',limit_choices_to={'catalogos': 14})
	cdu_municipio_dom = models.ForeignKey(CatalogoDetalle,to_field='cdu_catalogo',default='0150000',related_name='pesonal_cdu_municipio',limit_choices_to={'catalogos': 15})
	imagen = models.ImageField(upload_to='personal',default='' ,blank=True)


#error_messages={'blank': 'INVALID!!11', 'null': 'NULL11!'})
	@property
	def nombre_completo(self):
		return '%s %s %s' % (self.paterno, self.materno,self.nombre)

	def str(self):
		return self.paterno + ' ' + self.materno + ' ' + self.nombre
	

	def __unicode__(self):
		return '(%d) %s %s %s' % (self.matricula,self.paterno, self.materno,self.nombre)

	def save(self, *args, **kwargs):	
		super(Personal, self).save(*args, **kwargs)


	class Meta:
		verbose_name = "personal" 
		verbose_name_plural = "personal"