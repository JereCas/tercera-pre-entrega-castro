# tercera-pre-entrega-castro

* Descripción:

Esta página web permite incorporar información a 3 clases diferentes utilizando un formulario para cada una.
Ademas, esta configurado para realizar búsquedas en cada uno de los 3 listados.

Está armada con una página de inicio y tres páginas más: Alumno, Profesores y Cursos. Todas vinculadas a traves de la barra superior.
Las mismas estas construidas con herencia HTML.

* Carga de datos y búsqueda:

Datos: Se configuró un archivo seed_data.py para realizar una carga inicial de datos en cada una de las clases.
Estos datos contienen algunos valores repetidos para probar el comportamiento de una búsqueda con dichos valores.

Busqueda: En cada página (Alumno, Profesor y Curso) hay un buscador que permite realizar búsquedas en cada una de las clases.
Dentro de cada formulario esta descripto el ítem a traves de cual se debe realizar la búsqueda, por apellido o por nombre de curso, segun corresponda.