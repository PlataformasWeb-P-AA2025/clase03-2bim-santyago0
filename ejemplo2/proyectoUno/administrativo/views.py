from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render

# importar las clases de models.py
from administrativo.models import *

# Create your views here.

def index(request):
    # return HttpResponse("Hola mundo desde Python")
    return HttpResponse("Hola mundo desde Python<br/>%s" % (request.path))

def listadoEstudiantes(request):
    """
    Listar los registros del modelo Estudiante, 
    obtenidos de la base de datos.
    """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # estudiantes
    estudiantes = Estudiante.objects.all()
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {'estudiantes': estudiantes, 'numero_estudiantes': len(estudiantes)}
    return render(request, 'administrativo/listadoEstudiantes.html', informacion_template)
    

def listadoEstudiantesDos(request):
    """
    Listar los registros del modelo Estudiante, 
    obtenidos de la base de datos.
    """
    estudiantes = Estudiante.objects.all()
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {'estudiantes': estudiantes, 'numero_estudiantes': len(estudiantes)}
    return render(request, 'administrativo/listadoEstudiantesDos.html', informacion_template)
 
