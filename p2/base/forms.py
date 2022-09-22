from django.forms import ModelForm
from .models import Curso, Estudiante, Prueba, Preguntas, EstudiantePreguntas, Tema

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

class EstudianteForm(ModelForm):
    class Meta:
        model = Estudiante
        fields = 'curso','nombres','apellidos','nombre_completo'    

class EstudiantePreguntasForm(ModelForm):
    class Meta:
        model = EstudiantePreguntas
        fields = '__all__'        

class PruebaForm(ModelForm):
    class Meta:
        model = Prueba
        fields = 'nombre_prueba',

class PreguntasForm(ModelForm):
    class Meta:
        model = Preguntas
        fields = ['prueba','tema','pregunta']

class TemaForm(ModelForm):
    class Meta:
        model = Tema
        fields = '__all__'
