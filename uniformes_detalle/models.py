from django.core.files import File
import urllib
from django.db import models
from django.contrib.auth.models import User
from audit_log.models.managers import AuditLog
from catalogos_detalle.models import CatalogoDetalle
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from uniformes.models import Uniforme

class UniformeDetalle(models.Model):
	uniforme = models.ForeignKey(Uniforme,related_name='detalle_uniforme', on_delete=models.PROTECT,null=True)
	cdu_concepto_uniforme =models.ForeignKey(CatalogoDetalle,to_field='cdu_catalogo',default='',related_name='uniformedetalle_cdu_uniforme',limit_choices_to={'catalogos': 31}, on_delete=models.PROTECT)

	def str(self):
		return self.uniforme
	
	def __unicode__(self):
		return '%d' % (self.id)