from django.urls import path

from . import views

urlpatterns = [
    
    path('', views.brochure, name="brochure"),
    path('administracion', views.administracion, name="administracion"),
    path('planes', views.administracionplanes, name="planes"),
   path('firma', views.administracionfirma, name="firma_electronica"),
   path('Evaluacion', views.administracionEvaluacion, name="Evaluacion"),
   path('Climaorganizacional', views.administracionClimaorganizacional, name="Climaorganizacional"),
   path('SeleccionyCapacitacion', views.administracionSeleccionyCapacitacion, name="SeleccionyCapacitacion"),
   path('finanzas', views.finanzas, name="finanzas"),
   path('Cuenta_a_pagar', views.finanzasCuenta, name="Cuenta_a_pagar"),
   path('Cuentas_por_cobrar', views.finanzasCobrar, name="Cuentas_por_cobrar"),
   path('facturacion', views.finanzasfacturacion, name="facturacion"),
   path('Reportes_faltante', views.finanzasReportes_faltantes, name="Reportes_faltante"),
    path('logistica', views.logistica, name="logistica"),
    path('Bodegas', views.logisticaBodega, name="Bodegas"),
    path('Inventarios', views.logisticaInventarios, name="Inventarios"),
    path('Repuestos', views.logisticaRepuestos, name="Repuestos"),
    path('Solicitudes_por_pedido', views.logisticaSolicitudes_por_pedido, name="Solicitudes_por_pedido"),
    path('comercial', views.comercial, name="comercial"),
    path('Cotizaciones', views.comercialCotizaciones, name="Cotizaciones"),
    path('CMR', views.comercialCMR, name="CMR"),
    path('prospección_de_Clientes', views.comercialprospección_de_Clientes, name="prospección_de_Clientes"),
    path('Fidelizacion_y_Post_Venta', views.comercialFidelizacion_y_Post_Venta, name="Fidelizacion_y_Post_Venta"),
    path('proyectos', views.proyectos, name="proyectos"),
    path('Control_de_tiempos_y_costos', views.comercialFidelizacion_y_Post_Venta, name="Control_de_tiempos_y_costos"),
    path('Control_documentario', views.proyectosControl_documentario, name="Control_documentario"),
    path('Gestion_de_riesgo', views.proyectosGestion_de_riesgo, name="Gestion_de_riesgo"),
    path('Gestion_de_valor_ganado', views.proyectosGestion_de_valor_ganado, name="Gestion_de_valor_ganado"),
    path('Planificación_de_poryectos', views.proyectosPlanificación_de_poryectos, name="Planificación_de_poryectos"),
    path('Tareas_de_personal', views.proyectosTareas_de_personal, name="Tareas_de_personal"),
    path('seguridad', views.seguridad, name="seguridad"),
    path('Habilitacion_de_personal', views.seguridadHabilitacion_de_personal, name="Habilitacion_de_personal"),
    path('Inspecciones', views.seguridadInspecciones, name="Inspecciones"),
    path('Procedimientos', views.seguridadProcedimientos, name="Procedimientos"),

]
