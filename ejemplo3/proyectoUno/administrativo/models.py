from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return "%s %s %s" % (self.nombre,
                self.apellido,
                self.cedula)

    def get_suma_cedula(self):
        return sum([int(s) for s in self.cedula])
    
    def get_inicial(self):
        return self.nombre[0]


class NumeroTelefonico(models.Model):
    telefono = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE,
    related_name="mis_numeros_telefonicos")

    def __str__(self):
        return "%s %s" % (self.telefono, self.tipo)
