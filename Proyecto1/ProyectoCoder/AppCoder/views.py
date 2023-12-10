from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Curso
from .forms import CursoFormulario
def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def cursos(request):
    return render(request, 'AppCoder/cursos.html')

def profesores(request):
    return render(request, 'AppCoder/profesores.html')

def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')

def entregables(request):
    return render(request, 'AppCoder/entregables.html')

def cursos_formulario(request):
    if request.method == 'POST':
        mi_formulario = CursoFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            curso = Curso(curso=informacion["curso"], camada=informacion["camada"])
            curso.save()
            return redirect('inicio')  # Redirige a la página de inicio después de guardar el formulario
    else:
        mi_formulario = CursoFormulario()

    return render(request, 'AppCoder/cursos_formulario.html', {"mi_formulario": mi_formulario})

