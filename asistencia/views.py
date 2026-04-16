from django.shortcuts import redirect, render

from .forms import AsistenciaForm


def registrar_asistencia(request):
    if request.method == "POST":
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/asistencia/confirmacion/")
    else:
        form = AsistenciaForm()

    return render(request, "asistencia/formulario_asistencia.html", {"form": form})
