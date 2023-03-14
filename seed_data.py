from Entrega_tres.models import Alumno, Profesor, Curso

Alumno(nombre_alumno="Martin",
      apellido_alumno="Perez",
      direccion_alumno="Bs.As",
      description="Descripcion M. Perez",
      ).save()
Alumno(nombre_alumno="Claudia",
      apellido_alumno="Sanchez",
      direccion_alumno="La Pampa",
      description="Descripcion C. Sanchez",
      ).save()
Alumno(nombre_alumno="Pablo",
      apellido_alumno="Mendez",
      direccion_alumno="La plata",
      description="Descripcion P. Mendez",
      ).save()
Alumno(nombre_alumno="Jorge",
      apellido_alumno="Mendez",
      direccion_alumno="Santa Fe",
      description="Descripcion J. Mendez",
      ).save()


Profesor(
    nombre_profesor = "Andres",
    apellido_profesor = "Gomez",
    direccion_profesor  = "Cordoba ",
    description = "Descripcion A. Gomez",
    ).save()
Profesor(
    nombre_profesor = "Juan",
    apellido_profesor = "Rodriguez",
    direccion_profesor  = "Salta",
    description = "Descripcion J. Rodriguez",
    ).save()
Profesor(
    nombre_profesor = "Silvia",
    apellido_profesor = "Rodriguez",
    direccion_profesor  = "Mendoza",
    description = "Descripcion S. Rodriguez",
    ).save()

Curso(
    nombre_curso = "Python",
    duracion_curso = "25 Clases",
    Profesor_asignado = "A. Gomez", 
    ).save() 
Curso(
    nombre_curso = "Matematica",
    duracion_curso = "20 Clases",
    Profesor_asignado = "J. Rodriguez", 
    ).save() 
Curso(
    nombre_curso = "CSS",
    duracion_curso = "20 Clases",
    Profesor_asignado = "S. Rodriguez", 
    ).save() 