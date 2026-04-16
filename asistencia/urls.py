from django.urls import path

from .views import registrar_asistencia

app_name = "asistencia"

urlpatterns = [
    path("registro/", registrar_asistencia, name="registrar_asistencia"),
]
