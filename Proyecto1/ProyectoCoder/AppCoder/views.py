from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppCoder.models import Curso
from .forms import CursoFormulario, EstudianteFormulario

# def inicio(request):
#     # Verifica si 'camada' está presente en request.GET
#     # if 'camada' in request.GET:
#     #     camada = request.GET['camada']
#     #     cursos = Curso.objects.filter(camada__icontains=camada)
#     #     return render(request, 'AppCoder/inicio.html', {'cursos': cursos, 'camada': camada})
#     # else:
#     #     # Si 'camada' no está presente, realiza alguna acción predeterminada
#     #     return render(request, 'AppCoder/inicio.html')


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


# def profesores(request):
#     return render(request, 'AppCoder/profesores.html')

# def estudiantes(request):
#     if request.method == 'POST':
#         # Si la solicitud es un POST, procesar el formulario
#         mi_formulario = EstudianteFormulario(request.POST)

#         if mi_formulario.is_valid():
#             # El formulario es válido, puedes acceder a los datos del formulario usando cleaned_data
#             nombre = mi_formulario.cleaned_data['nombre']
#             apellido = mi_formulario.cleaned_data['apellido']
#             email = mi_formulario.cleaned_data['email']

#             # Aquí puedes realizar acciones con los datos del formulario, como guardar en la base de datos

#             # Redirigir a alguna página de éxito o volver a cargar la misma página
#             return redirect('inicio.htmlcls')  # Reemplaza 'nombre_de_tu_vista_exito' con la vista de éxito

#     else:
#         # Si la solicitud no es un POST, simplemente renderizar el formulario vacío
#         mi_formulario = EstudianteFormulario()

#     return render(request, 'AppCoder/estudiantes.html', {'mi_formulario': mi_formulario})

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

# def buscar_camada(request):
#     return render(request, "AppCoder/buscar_camada.html")

# def buscar(request):
#     if request.GET["camada"]:
#         camada = request.GET['camada']
#         cursos = Curso.objects.filter(camada__icontains=camada)

#         return render(request, 'AppCoder/resultadosBusqueda.html', {'cursos': cursos, 'camada': camada})
     
#     else:
#         respuesta = 'No enviaste datos.'
#         return HttpResponse(respuesta)

class FormularioEstudianteView:
    def index(request):
        estudiante = EstudianteFormulario()
        return render(request, "estudiantes.html", {"form": estudiante})
    
    def procesar_formulario(request):
        estudiante = EstudianteFormulario(request.POST)
        if estudiante.is_valid():
            estudiante.save()
            estudiante = EstudianteFormulario()

        return render(request, "estudiantes.html", {"form": estudiante, "mensaje": 'OK'})
