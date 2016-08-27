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
	cubre = models.ForeignKey("Incidencia",  default=None, null=True,blank=True, related_name="cubre_a")

	def str(self):
		return self.id_personal + ' ' + self.fecha
	
	def __unicode__(self):
		return '(%s) %s' % (self.id_personal,self.fecha)


	class Meta:
		unique_together = ('id_personal', 'fecha',)
# q=Incidencia.objects.filter(id_personal__paterno__contains='TORRES',fecha='2016-03-12')
#qs = Personal.objects.all()
#		for valor in valor_buscado.split():
#			qs=qs.filter(Q(paterno__icontains = valor) | Q(materno__icontains = valor) | Q(nombre__icontains = valor) )
#		return qs

#Personal.objects.filter(personalsucursal_id_personal__fecha_inicial__gte='2015-08-18')
#from datetime import datetime, date
#inicial = date(2016, 3, 18)
#final = date(1900,1,1	)

#q=Incidencia.objects.filter(id_personal__personalsucursal_id_personal__fecha_inicial='2015-08-18')
#
# q = q.filter(Q(personalsucursal_id_personal__fecha_inicial__gte=inicial) | Q(personalsucursal_id_personal__fecha_final=final))
# q = Personal.objects.all()
# q = q.filter(Q(personalsucursal_id_personal__fecha_inicial__gte=inicial ,personalsucursal_id_personal__fecha_final__lt=inicial)| Q(personalsucursal_id_personal__fecha_inicial__gte=inicial ,personalsucursal_id_personal__fecha_final=final))

# q = Incidencia.objects.all()
# q = q.filter(Q(fecha=inicial), Q(id_personal__personalsucursal_id_personal__fecha_inicial__gte=inicial,id_personal__personalsucursal_id_personal__fecha_final__lt=inicial)| Q(id_personal__personalsucursal_id_personal__fecha_inicial__lte=inicial ,id_personal__personalsucursal_id_personal__fecha_final=final))
# from incidencias.models import Incidencia
# from datetime import datetime, date
# inicial = date(2016, 3, 18)
# final = date(1900,1,1	)


#********************
# from django.db.models import Q
# q = Incidencia.objects.all().values('id','fecha','cdu_concepto_incidencia','cdu_concepto_incidencia__descripcion1','observaciones',id_personal__personalsucursal_id_personal__cdu_motivo','id_personal__personalsucursal_id_personal__cdu_motivo__descripcion1')
# q = q.filter(Q(fecha=inicial), Q(id_personal__personalsucursal_id_personal__fecha_inicial__lte=inicial,id_personal__personalsucursal_id_personal__fecha_final__gt=inicial)| Q(id_personal__personalsucursal_id_personal__fecha_inicial__lte=inicial ,id_personal__personalsucursal_id_personal__fecha_final=final))

#q = Incidencia.objects.all().values('id','fecha','cdu_concepto_incidencia','cdu_concepto_incidencia__descripcion1','observaciones','id_personal__personalsucursal_id_personal__cdu_turno','id_personal__personalsucursal_id_personal__cdu_turno__descripcion1','id_personal__personalsucursal_id_personal__cdu_puesto','id_personal__personalsucursal_id_personal__cdu_puesto__descripcion1','id_personal__personalsucursal_id_personal__id_sucursal','id_personal__personalsucursal_id_personal__id_sucursal__nombre')
# q = q.filter(Q(fecha=inicial), Q(id_personal__personalsucursal_id_personal__fecha_inicial__lte=inicial,id_personal__personalsucursal_id_personal__fecha_final__gt=inicial)| Q(id_personal__personalsucursal_id_personal__fecha_inicial__lte=inicial ,id_personal__personalsucursal_id_personal__fecha_final=final))



# q = Incidencia.objects.select_related('cdu_concepto_incidencia').filter(fecha=inicial,personalsucursal_id_personal__fecha_final__lt=inicial)

#q= Incidencia.objects.prefetch_related('personal_set')

#q = Incidencia.objects.select_related('cdu_concepto_incidencia','id_personal__personalsucursal').filter(fecha=inicial,id_personal__personalsucursal_id_personal__fecha_final__lte=inicial)

# id
# fecha
# cdu_concepto_incidencia_id
# id_personal_id
# cdu_turno
# cdu_puesto
# id_sucursal_id
#Incidencia.objects.select_related('cdu_concepto_incidencia','id_personal').filter(fecha__gte=fecha_ini,fecha__lte=fecha_fin).order_by('fecha','id_personal__paterno')
#ModelB.objects.select_related('a').all() # Forward ForeignKey relationship
#ModelA.objects.prefetch_related('modelb_set').all(


#  q = Incidencia.objects.values('id','id_personal__personalsucursal_id_personal').all()
#  q = q.filter(Q(id_personal__personalsucursal_id_personal__fecha_inicial__lte=inicial))

# q = Incidencia.objects.values('id','id_personal__personalsucursal_id_personal__cdu_motivo').all()
#q = Incidencia.objects.values('id','id_personal__personalsucursal_id_personal__cdu_motivo__descripcion1').all()

# q = Incidencia.objects.extra(select={'variable':"'id_personal__personalsucursal_id_personal__fecha_final'"}).filter(fecha=inicial,id_personal__personalsucursal_id_personal__fecha_final__lte=inicial)
