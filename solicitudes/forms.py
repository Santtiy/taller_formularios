from django import forms

from .models import Solicitud


class SolicitudForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = [
            "nombre_solicitante",
            "documento_identidad",
            "correo_electronico",
            "telefono_contacto",
            "tipo_solicitud",
            "asunto",
            "descripcion_detallada",
            "fecha_solicitud",
            "archivo_adjunto",
        ]
        labels = {
            "nombre_solicitante": "Nombre del solicitante",
            "documento_identidad": "Documento de identidad",
            "correo_electronico": "Correo electronico",
            "telefono_contacto": "Telefono de contacto",
            "tipo_solicitud": "Tipo de solicitud",
            "asunto": "Asunto",
            "descripcion_detallada": "Descripcion detallada",
            "fecha_solicitud": "Fecha de solicitud",
            "archivo_adjunto": "Archivo adjunto (opcional)",
        }
        help_texts = {
            "archivo_adjunto": "Puedes subir un archivo de soporte si lo necesitas.",
        }
        widgets = {
            "nombre_solicitante": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ejemplo: Maria Gomez",
                }
            ),
            "documento_identidad": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ejemplo: 1000123456",
                }
            ),
            "correo_electronico": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ejemplo: correo@dominio.com",
                }
            ),
            "telefono_contacto": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ejemplo: 3001234567",
                }
            ),
            "tipo_solicitud": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
            "asunto": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Resumen breve de la solicitud",
                }
            ),
            "descripcion_detallada": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 6,
                    "placeholder": "Explica tu solicitud con el mayor detalle posible.",
                }
            ),
            "fecha_solicitud": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),
            "archivo_adjunto": forms.ClearableFileInput(
                attrs={
                    "class": "form-control file-control",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["tipo_solicitud"].empty_label = "Selecciona una opcion"
