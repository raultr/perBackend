# -*- encoding: utf-8 -*-
from django.core.exceptions import ValidationError
import urllib
from django.db import transaction
from django.contrib.auth.models import User
from audit_log.models.managers import AuditLog
from django.db import models
from catalogos_detalle.models import CatalogoDetalle
from personal.models import Personal

class Incidencia(models.Model):
	id_personal = models.ForeignKey(Personal,related_name='personalincidencia_id_personal', on_delete=models.PROTECT)
	cdu_concepto_incidencia =models.ForeignKey(CatalogoDetalle,to_field='cdu_catalogo',default='',related_name=' personalincidencia_cdu_motivo',limit_choices_to={'catalogos': 30}, on_delete=models.PROTECT)
	fecha = models.DateField(default = '1900-01-01')
	observaciones = models.CharField(max_length=200,blank=True)

	class Meta:
		unique_together = ('id_personal', 'fecha',)