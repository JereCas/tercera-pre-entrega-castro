from django.shortcuts import render
from Entrega_tres.models import Alumno, Profesor, Curso
from Entrega_tres.forms import AlumnoForm, ProfesorForm, CursoForm 

def index (request):
    return render (request, "Entrega_tres/index.html")

# def alumnos

def alumnos(request):
    context = {
        "form": AlumnoForm(),
        "alumnos": Alumno.objects.all(),

    }
    alumnos = Alumno.objects.all()
    return render (request, "Entrega_tres/alumnos.html", context)

def agregar_alumno(request):
    alumno_form = AlumnoForm(request.POST)
    alumno_form.save()    
    context = {
        "form": AlumnoForm(),
        "alumnos": Alumno.objects.all(),
    }
    return render (request, "Entrega_tres/alumnos.html", context)

def buscar_alumno(request):
    criterio = request.GET.get("criterio")
    context = {
    "alumnos": Alumno.objects.filter(apellido_alumno__icontains=criterio).all(),

    }
    return render (request, "Entrega_tres/alumnos.html", context)


# def profesores 

def profesores(request):
    context = {
        "form": ProfesorForm(),
        "profesores": Profesor.objects.all(),

    }
    profesores = Profesor.objects.all()
    return render (request, "Entrega_tres/profesores.html", context)

def agregar_profesor(request):
    profesor_form = ProfesorForm(request.POST)
    profesor_form.save()    
    context = {
        "form": ProfesorForm(),
        "profesores": Profesor.objects.all(),
    }
    return render (request, "Entrega_tres/profesores.html", context)

def buscar_profesor(request):
    criterio = request.GET.get("criterio")
    context = {
    "profesores": Profesor.objects.filter(apellido_profesor__icontains=criterio).all(),

    }
    return render (request, "Entrega_tres/profesores.html", context)

# def cursos 

def cursos(request):
    context = {
        "form": CursoForm(),
        "cursos": Curso.objects.all(),
    }
    cursos = Curso.objects.all()
    return render (request, "Entrega_tres/cursos.html", context)

def agregar_curso(request):
    curso_form = CursoForm(request.POST)
    curso_form.save()    
    context = {
        "form": CursoForm(),
        "cursos": Curso.objects.all(),
    }
    return render (request, "Entrega_tres/cursos.html", context)

def buscar_curso(request):
    criterio = request.GET.get("criterio")
    context = {
    "cursos": Curso.objects.filter(nombre_curso__icontains=criterio).all(),

    }
    return render (request, "Entrega_tres/cursos.html", context)