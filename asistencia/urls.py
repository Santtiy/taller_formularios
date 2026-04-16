from django.urls import path

from .views import confirmacion_asistencia, registrar_asistencia

app_name = "asistencia"

urlpatterns = [
    path("registro/", registrar_asistencia, name="registrar_asistencia"),
    path("confirmacion/", confirmacion_asistencia, name="confirmacion_asistencia"),
]
