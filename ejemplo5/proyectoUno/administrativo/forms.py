from django.forms import ModelForm
from django import forms

from administrativo.models import Estudiante, \
        NumeroTelefonico

"""

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return "%s %s %s" % (self.nombre,
                self.apellido,
                self.cedula)
"""
class EstudianteForm(ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'cedula'] 


class NumeroTelefonicoForm(ModelForm):
    class Meta:
        model = NumeroTelefonico
        fields = ['telefono', 'tipo', 'estudiante']


class NumeroTelefonicoEstudianteForm(ModelForm):

    def __init__(self, estudiante, *args, **kwargs):
        super(NumeroTelefonicoEstudianteForm, self).__init__(*args, **kwargs)
        self.initial['estudiante'] = estudiante
        self.fields["estudiante"].widget = forms.widgets.HiddenInput()
        print(estudiante)

    class Meta:
        model = NumeroTelefonico
        fields = ['telefono', 'tipo', 'estudiante']
