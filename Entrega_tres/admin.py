from django.contrib import admin
from Entrega_tres.models import Alumno
from Entrega_tres.models import Profesor
from Entrega_tres.models import Curso

admin.site.register(Alumno)
admin.site.register(Profesor)
admin.site.register(Curso)