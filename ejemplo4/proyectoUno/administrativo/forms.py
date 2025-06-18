from django.forms import ModelForm
from administrativo.models import Estudiante


class EstudianteForm(ModelForm): 
    class Meta:
        model = Estudiante 
        fields = ['nombre', 'apellido', 'cedula'] 




