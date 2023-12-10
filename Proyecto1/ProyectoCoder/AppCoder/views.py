from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso
from .forms import CursoFormulario

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def cursos(request):
    if request.method == 'POST':
        mi_formulario = CursoFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            curso = Curso(nombre=informacion["nombre"], camada=informacion["camada"])
            curso.save()
            return render(request, 'AppCoder/inicio.html')
    else:
        mi_formulario = CursoFormulario()
        return render(request, 'AppCoder/cursos.html', {"mi_formulario": mi_formulario})

# def cursos(request):

#  if request.method == 'POST':
         
#          mi_formulario = CursoFormulario(request.POST)
#          if mi_formulario.is_valid():
#              curso = mi_formulario.cleaned_data
#              curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
#              curso.save()
#              return render(request, 'AppCoder/inicio.html')
#          else:
#                 mi_formulario = CursoFormulario()
#                 return render(request, 'AppCoder/cursos.html', {"mi_formulario": mi_formulario})


def profesores(request):
    return render(request, 'AppCoder/profesores.html')

def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')

def entregables(request):
    return render(request, 'AppCoder/entregables.html')

# def cursos_formulario(request):
#      if request.method == 'POST':
         
#          mi_formulario = CursoFormulario(request.POST)
#          if mi_formulario.is_valid():
#              curso = mi_formulario.cleaned_data
#              curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
#              curso.save()
#              return render (request, 'AppCoder/inicio.html')
#      else:
#          mi_formulario = CursoFormulario()
#          return render(request, 'AppCoder/cursos_formulario.html', {"mi_formulario": mi_formulario})

def buscar_camada(request):
    return render(request, "AppCoder/buscar_camada.html")

def buscar(request):
    if request.GET["camada"]:
        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada__icontains=camada)

        return render(request, 'AppCoder/resultadosBusqueda.html', {'cursos': cursos, 'camada': camada})
     
    else:
        respuesta = 'No enviaste datos.'
        return HttpResponse(respuesta)
