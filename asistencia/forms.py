from django import forms

from .models import Asistencia


class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = [
            "nombre_completo",
            "documento_identidad",
            "correo_electronico",
            "fecha_asistencia",
            "hora_ingreso",
            "hora_salida",
            "presente",
            "observaciones",
        ]
        labels = {
            "nombre_completo": "Nombre completo",
            "documento_identidad": "Documento de identidad",
            "correo_electronico": "Correo electronico",
            "fecha_asistencia": "Fecha de asistencia",
            "hora_ingreso": "Hora de ingreso",
            "hora_salida": "Hora de salida",
            "presente": "Confirmo que la persona estuvo presente",
            "observaciones": "Observaciones",
        }
        help_texts = {
            "documento_identidad": "Ingresa numero de documento o codigo alfanumerico.",
            "observaciones": "Campo opcional para anotar novedades.",
        }
        widgets = {
            "nombre_completo": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej. Maria Lopez",
                    "autocomplete": "name",
                }
            ),
            "documento_identidad": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej. 1020304050",
                }
            ),
            "correo_electronico": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ej. correo@dominio.com",
                    "autocomplete": "email",
                }
            ),
            "fecha_asistencia": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),
            "hora_ingreso": forms.TimeInput(
                attrs={
                    "class": "form-control",
                    "type": "time",
                }
            ),
            "hora_salida": forms.TimeInput(
                attrs={
                    "class": "form-control",
                    "type": "time",
                }
            ),
            "presente": forms.CheckboxInput(attrs={"class": "checkbox-input"}),
            "observaciones": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Escribe aqui comentarios adicionales (opcional).",
                }
            ),
        }
