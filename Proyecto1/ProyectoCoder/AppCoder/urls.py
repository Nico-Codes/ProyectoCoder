from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('cursos/', views.cursos, name="cursos"),
    path('profesores/', views.profesores, name="profesores"),
    path('estudiantes/', views.estudiantes, name="estudiantes"),
    path('entregables/', views.entregables, name="entregables"),
    # path('cursosFormulario/', views.cursos_formulario, name="Cursos formulario"),
    path('buscarCamada/', views.buscar_camada, name="Buscar Camada"),
    path('buscar/', views.buscar),


]
