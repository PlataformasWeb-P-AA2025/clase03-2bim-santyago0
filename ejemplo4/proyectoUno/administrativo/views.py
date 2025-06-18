from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render

# importar las clases de models.py
from administrativo.models import *

# importar los formularios de forms.py
from administrativo.forms import *

# Create your views here.

def index(request):
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
    return render(request, 'index.html', informacion_template)


def obtener_estudiante(request, id):
    """
        Listar los registros del modelo Estudiante,
        obtenidos de la base de datos.
    """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # estudiantes
    estudiante = Estudiante.objects.get(pk=id)
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {'estudiante': estudiante}
    return render(request, 'obtener_estudiante.html', informacion_template)


def crear_estudiante(request):
    """
    """
    print(request)
    if request.method=='POST':
        formulario = EstudianteForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = EstudianteForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearEstudiante.html', diccionario)


def editar_estudiante(request, id):
    """
    """
    print("---------------")
    print(request)
    print("---------------")
    estudiante = Estudiante.objects.get(pk=id)
    # Deber: consultar
    if request.method=='POST':
        formulario = EstudianteForm(request.POST, instance=estudiante)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = EstudianteForm(instance=estudiante)
    diccionario = {'formulario': formulario}

    return render(request, 'editarEstudiante.html', diccionario)


def eliminar_estudiante(request, id):
    """
    """
    estudiante = Estudiante.objects.get(pk=id)
    estudiante.delete()
    return redirect(index)

# TALLER CLASE03
# Listar Pais
# Crear Pais con formulario

def index2(request):
    """
        Listar los registros del modelo Pais,
        obtenidos de la base de datos.
    """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # estudiantes
    paises = Pais.objects.all()
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {'paises': paises, 'numero_paises': len(paises)}
    return render(request, 'index2.html', informacion_template)

def obtener_pais(request, id):
    """
        Listar los registros del modelo Pais,
        obtenidos de la base de datos.
    """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # estudiantes
    pais = Pais.objects.get(pk=id)
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {'pais': pais}
    return render(request, 'obtener_pais.html', informacion_template)


def crear_pais(request):
    """
    """
    print(request)
    if request.method=='POST':
        formulario = PaisForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index2)
    else:
        formulario = PaisForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearPais.html', diccionario)
