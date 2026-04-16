from django.urls import path

from .views import confirmacion_solicitud, registrar_solicitud

app_name = "solicitudes"

urlpatterns = [
    path("registro/", registrar_solicitud, name="registrar_solicitud"),
    path("confirmacion/", confirmacion_solicitud, name="confirmacion_solicitud"),
]
