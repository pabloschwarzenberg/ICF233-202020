# Servicio de Planificación

Este servicio permite el registro de cursos y sus NRC asociados para el servicio de inscripción de asignaturas.

Para ejecutar las pruebas:

python manage.py test -v 2

Para calcular la cobertura de las pruebas (el comando se debe ejecutar en la raíz de la carpeta del proyecto, después de instalar los paquetes en requirements.txt):

coverage run --source="." manage.py test api

Luego para ver el reporte de cobertura ejecutar:

coverage report