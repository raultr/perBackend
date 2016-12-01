from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import PermissionDenied
from datetime import datetime, date
import datetime
from django.db import IntegrityError,transaction,connection
from .models import Uniforme
from uniformes_detalle.models import UniformeDetalle
from catalogos_detalle.models import CatalogoDetalle
from .serializers import UniformeSerializer,UniformeDetalleSerializer,UniformeSerializerReporte

class UniformeConDetallesLista(APIView):
	def get(self, request, pk=None, format=None):
		if(pk!=None):
			print(pk)

		queryset = Uniforme.objects.all()
		serializer_class = UniformeSerializer(queryset,many=True)
		return  Response(serializer_class.data)
	
	def post(self, request, format=None):
		serializer_class = UniformeSerializer(data=request.DATA)
		if serializer_class.is_valid():
			try:
				with transaction.atomic():
					datos = request.DATA
					uniformes= Uniforme.objects.filter(id_personal=datos['id_personal'],anio=datos['anio'],periodo=datos['periodo'])
					if uniformes.first():
						uniforme = uniformes.first()
						uniforme.observaciones = datos['observaciones']
						uniforme.fecha = datetime.datetime.strptime(datos['fecha'],'%d/%m/%Y').strftime('%Y-%m-%d')
						uniforme.fecha_servicio = datetime.datetime.strptime(datos['fecha_servicio'],'%d/%m/%Y').strftime('%Y-%m-%d')
						
						uniforme.save()
					else:
						response = serializer_class.save()
						uniforme = Uniforme.objects.get(id=response.id)	
					existe_detalle = UniformeDetalle.objects.filter(uniforme=uniforme.pk)
					if existe_detalle.count()>0:
						raise PermissionDenied

 					UniformeDetalle.objects.filter(uniforme=uniforme.pk).delete()
					uniforme_detalle_datos = request.DATA.pop('detalle_uniforme')
					for detalle_datos in uniforme_detalle_datos:
						catalogo_uniforme = CatalogoDetalle.objects.get(cdu_catalogo=detalle_datos['cdu_concepto_uniforme'])
						UniformeDetalle.objects.create(uniforme=uniforme,cdu_concepto_uniforme=catalogo_uniforme)

					queryset = Uniforme.objects.filter(pk=uniforme.pk)
					datos =  UniformeSerializer(queryset,many=True)

				return Response(datos.data, status=status.HTTP_201_CREATED)
			except IntegrityError as ex:
				return Response({'error': str(ex)}, status=status.HTTP_403_FORBIDDEN)
			except PermissionDenied as ex:
				return Response({"Los uniformes asignados no se pueden modificar"}, status=status.HTTP_403_FORBIDDEN)
			except Exception as ex:
				return Response({'error': str(ex)}, status=status.HTTP_403_FORBIDDEN)
		return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonalUniformeConDetalles(APIView):
	def get(self, request, pk=None, format=None):
		campos = {}
		if 'id_personal' in request.GET:
			campos['id_personal'] = request.GET['id_personal']
		if 'anio' in request.GET:
			campos['anio'] = request.GET['anio']
		if 'periodo' in request.GET:
			campos['periodo'] = request.GET['periodo']
		queryset = Uniforme.objects.filter(**campos )
		serializer_class = UniformeSerializer(queryset,many=True)
		return  Response(serializer_class.data)


class UniformeConDetallesListaReporte(APIView):
	def get(self, request, pk=None, format=None):
		if(pk!=None):
			print(pk)

		queryset = Uniforme.objects.all()
		serializer_class = UniformeSerializerReporte(queryset,many=True)
		return  Response(serializer_class.data)

class UniformeReporteGeneral(APIView):
	def get(self ,request):
		anio = request.GET['anio']
		periodo = request.GET['periodo']


		cursor = connection.cursor()

		columnas ="""
			select  case when cunif.id is null then 'No' else 'Si' end as ent,cunif.id_personal_id,perso.matricula,perso.paterno,perso.materno,perso.nombre,
       		suc_act.sucursal,suc_act.cdu_motivo,suc_act.motivo,
            cunif.id,cunif.fecha,cunif.anio,cunif.periodo,cunif.observaciones,cunif.fecha_servicio ,
            dunif.entregado,suc_fecha.id_sucursal_id,suc_det_fecha.nombre as sucursal_fecha
			"""
		tabla_principal = "from personal_personal as perso"

		rel_suc_activa = """
			 left join(
			 	select asig.id_personal_id,asig.id_sucursal_id,suc.nombre as sucursal,asig.cdu_motivo_id as cdu_motivo,cmotivo.descripcion1 as motivo
			 	 from personal_sucursales_personalsucursal as asig
			 	 left join sucursales_sucursal as suc
			 	 on suc.id = asig.id_sucursal_id
			 	 left join catalogos_detalle_catalogodetalle as cmotivo
			 	 on cmotivo.cdu_catalogo = asig.cdu_motivo_id
			 	where fecha_final='01/01/1900'
			 	) as suc_act on suc_act.id_personal_id = perso.id
		"""

		rel_uniformes="""
			 left join uniformes_uniforme as cunif on perso.id = cunif.id_personal_id 
			 and cunif.anio=%s and cunif.periodo=%s
			 left join(
			 	select udet.uniforme_id,string_agg(dunif.descripcion1, ',') as entregado
			 	from uniformes_detalle_uniformedetalle as udet
			 	join catalogos_detalle_catalogodetalle dunif 
			 	on dunif.catalogos_id=31 and 
			 	dunif.cdu_catalogo = udet.cdu_concepto_uniforme_id
			 	group by udet.uniforme_id
			 	) as dunif on dunif.uniforme_id = cunif.id
		"""

		rel_suc_fec_uniforme = """
 			left join personal_sucursales_personalsucursal as suc_fecha
			 on  suc_fecha.id_personal_id =perso.id and 
			  ((cunif.fecha_servicio>=suc_fecha.fecha_inicial  and cunif.fecha_servicio<=suc_fecha.fecha_final)
			 or (cunif.fecha_servicio>=suc_fecha.fecha_inicial  and suc_fecha.fecha_final='01/01/1900'))
			 left join sucursales_sucursal as suc_det_fecha 
			 on suc_det_fecha.id = suc_fecha.id_sucursal_id
		"""
		orden =" order by perso.paterno,perso.materno,perso.nombre"

		consulta = columnas + tabla_principal + rel_suc_activa + rel_uniformes +rel_suc_fec_uniforme + orden
#		condicion = ""

#		orden =" order by inv.num_rollo,ventadc.id"
		
#		condicion_por_num_rollo = """
#					where lower(inv.num_rollo) like lower( %s)
#				"""
#		if(num_rollo != ""):
#			condicion = condicion_por_num_rollo
#			consulta = columnas + condicion + orden
#			num_rollo = '%' + num_rollo + '%'
#			cursor.execute(consulta,[num_rollo])
#			resultado = self.dictfetchall(cursor)
#			return  Response(data=resultado, status=status.HTTP_201_CREATED)

#		consulta = columnas + condicion + orden
		cursor.execute(consulta,[anio,periodo])
		#resultado= cursor.fetchall()
		resultado = self.dictfetchall(cursor)
		#resultado = Existencia.objects.values('num_rollo').annotate(entradas_kd=Sum('entrada_kg'),salidas_kg=Sum('salida_kg'),existencia_kg=Sum('entrada_kg')-Sum('salida_kg'))
		return  Response(data=resultado, status=status.HTTP_201_CREATED)

	def dictfetchall(self,cursor):
		"Return all rows from a cursor as a dict"
		columns = [col[0] for col in cursor.description]
		return [
			dict(zip(columns, row))
			for row in cursor.fetchall()
		]

# select cunif.id_personal_id,perso.matricula,perso.paterno,perso.materno,perso.nombre,
#        suc_act.sucursal,suc_act.motivo,
#        cunif.id,cunif.fecha,cunif.anio,cunif.periodo,cunif.observaciones,cunif.fecha_servicio ,
#        dunif.entregado,suc_fecha.id_sucursal_id,suc_det_fecha.nombre as sucursal_fecha
# from personal_personal as perso
# left join(
# 	select asig.id_personal_id,asig.id_sucursal_id,suc.nombre as sucursal,cmotivo.descripcion1 as motivo
# 	 from personal_sucursales_personalsucursal as asig
# 	 left join sucursales_sucursal as suc
# 	 on suc.id = asig.id_sucursal_id
# 	 left join catalogos_detalle_catalogodetalle as cmotivo
# 	 on cmotivo.cdu_catalogo = asig.cdu_motivo_id
# 	where fecha_final='01/01/1900'
# 	) as suc_act on suc_act.id_personal_id = perso.id
# left join uniformes_uniforme as cunif on perso.id = cunif.id_personal_id --and cunif.anio=2015 and cunif.periodo=2
# left join(
# 	select udet.uniforme_id,string_agg(dunif.descripcion1, ',') as entregado
# 	from uniformes_detalle_uniformedetalle as udet
# 	join catalogos_detalle_catalogodetalle dunif 
# 	on dunif.catalogos_id=31 and 
# 	dunif.cdu_catalogo = udet.cdu_concepto_uniforme_id
# 	group by udet.uniforme_id
# 	) as dunif on dunif.uniforme_id = cunif.id
# left join personal_sucursales_personalsucursal as suc_fecha
# on  (cunif.fecha_servicio>=suc_fecha.fecha_inicial  and cunif.fecha_servicio<=suc_fecha.fecha_final)
# or (cunif.fecha_servicio>=suc_fecha.fecha_inicial  and suc_fecha.fecha_final='01/01/1900')
# left join sucursales_sucursal as suc_det_fecha 
# on suc_det_fecha.id = suc_fecha.id_sucursal_id

#motivo de baja 0250003
# Para los que no se les entro en uniforme no mostrar los que ya estan dados de baja