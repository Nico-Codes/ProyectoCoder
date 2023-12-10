from django import forms
from .models import Estudiante

class CursoFormulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()

class EstudianteFormulario(forms.ModelForm):
    class Meta:
        model = Estudiante  # Asegúrate de que el modelo Estudiante esté importado correctamente
        fields = '__all__'
        widgets = {'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'})}