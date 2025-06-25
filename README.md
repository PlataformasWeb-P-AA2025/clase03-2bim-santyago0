# clase03-2bim

## Captura:
![related_name](https://github.com/user-attachments/assets/3a08e1af-a956-47a8-938c-23923bf8b58d)

En la línea 8 del código de la imagen, se usa `e.numerotelefonico_set.all`, esto para poder obtener los números teléfonicos de los estudiantes cuando dentro del ForeingKey de no especificamos un `retated_name`


### 25 junio 2025
Para crear nuevos nnúmeros de teléfonos a un estudiante ya creado, lo que se debe hacer es:

En una función del `views.py` cargar un estudiante en específico a través de su id. Una vez cargado podemos acceder al formulario que nos permita agregar un número de teléfono a un estudiante en específico, y dentro de este formuraio podemos hacer que se oculte el campo de **estudiante**, ya que este está asociado al cliente que se cargó, no hace falta agregarle este campo a la hora de crear un nuevo teléfono.