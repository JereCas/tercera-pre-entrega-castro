from django.db import models

class Alumno(models.Model):
    nombre_alumno = models.CharField(max_length=30)
    apellido_alumno= models.CharField(max_length=80)
    direccion_alumno = models.CharField(max_length=30)
    description = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.id} - {self.apellido_alumno}"
    

class Profesor(models.Model):
    nombre_profesor = models.CharField(max_length=30)
    apellido_profesor = models.CharField(max_length=80)
    direccion_profesor  = models.CharField(max_length=30)
    description = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.id} - {self.apellido_profesor}"
    
class Curso(models.Model):
    nombre_curso = models.CharField(max_length=80)
    duracion_curso = models.CharField(max_length=80)
    Profesor_asignado = models.CharField(max_length=40)  

    def __str__(self):
        return f"{self.id} - {self.nombre_curso}"