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
	curp = models.CharField(max_length=8)
	cuip = models.CharField(max_length=30)
	fec_nacimiento =models.DateField(auto_now_add = '01/01/1900')
	cdu_estado_nac = models.ForeignKey(CatalogoDetalle,to_field='cdu_catalogo',default='',related_name='pesonal_cdu_estado_nac',limit_choices_to={'catalogos': 14},validators=[RegexValidator(regex='(?=^.{7,7}$)(^014)([0-9]{4})', message='El catalogo debe empezar con 14 y su longitud de 7', code='nomatch')])						
	cdu_municipio_nac =models.ForeignKey(CatalogoDetalle,to_field='cdu_catalogo',default='',related_name='pesonal_cdu_municipio_nac',limit_choices_to={'catalogos': 15})
	cdu_escolaridad =models.ForeignKey(CatalogoDetalle,to_field='cdu_catalogo',default='',related_name='pesonal_cdu_escolaridad',limit_choices_to={'catalogos': 2})
	cdu_religion = models.ForeignKey(CatalogoDetalle,to_field='cdu_catalogo',default='',related_name='pesonal_cdu_religion',limit_choices_to={'catalogos': 16})
	cdu_seguridad_social = models.ForeignKey(CatalogoDetalle,to_field='cdu_catalogo',default='',related_name='pesonal_cdu_seguridad_social',limit_choices_to={'catalogos': 17})
	id_seguridad_social =models.CharField(max_length=20)
	portacion = models.BooleanField(default=False)

	@property
	def nombre_completo(self):
		return '%s %s %s' % (self.paterno, self.materno,self.nombre)

	def str(self):
		return self.paterno + ' ' + self.materno + ' ' + self.nombre


	class Meta:
		verbose_name = "personal" 
		verbose_name_plural = "personal"