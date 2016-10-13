from django.core.files import File
import urllib
from django.db import models
from django.db import transaction
from django.contrib.auth.models import User
from audit_log.models.managers import AuditLog
from catalogos_detalle.models import CatalogoDetalle
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from personal.models import Personal


class Uniforme(models.Model):
	id_personal = models.ForeignKey(Personal,related_name='personaluniforme_id_personal', on_delete=models.PROTECT,null=True)
	fecha = models.DateField(default = '1900-01-01')
	anio = models.IntegerField(default=0)
	periodo = models.IntegerField(default=0)
	observaciones = models.CharField(max_length=200,blank=True)

	def str(self):
		return self.id

	def __unicode__(self):
		return '%d' % (self.id)
