"""
EJERCICIOS - DICCIONARIOS Y SETS EN PYTHON
===========================================
Resuelve cada ejercicio. No mires las soluciones hasta terminar.
"""

# ==============================================================================
# EJERCICIO 1: Creación y acceso
# ==============================================================================
# Crea un diccionario 'libro' con las claves: 'titulo', 'autor', 'año', 'genero'.
# Imprime:
# - El título del libro usando []
# - El autor usando get()
# - El ISBN usando get() con valor por defecto "No disponible"

# Tu código aquí:



# ==============================================================================
# EJERCICIO 2: Modificación y eliminación
# ==============================================================================
# Tienes el diccionario: estudiante = {"nombre": "Luis", "edad": 20, "cursos": ["Python"]}
# Realiza en orden:
# 1. Agrega la clave "promedio" con valor 85.5
# 2. Actualiza la edad a 21 usando update()
# 3. Agrega "JavaScript" a la lista de cursos
# 4. Elimina la clave "edad" usando pop()
# Imprime el diccionario final.

estudiante: dict = {"nombre": "Luis", "edad": 20, "cursos": ["Python"]}

# Tu código aquí:



# ==============================================================================
# EJERCICIO 3: Iteración y filtrado
# ==============================================================================
# Tienes el diccionario de productos y precios:
# productos = {"Laptop": 999, "Mouse": 25, "Teclado": 75, "Monitor": 300, "Webcam": 60}
# Crea e imprime:
# - Una lista con los nombres de productos cuyo precio sea mayor a 50
# - El precio total de todos los productos
# - El producto más caro y el más barato

productos: dict = {"Laptop": 999, "Mouse": 25, "Teclado": 75, "Monitor": 300, "Webcam": 60}

# Tu código aquí:



# ==============================================================================
# EJERCICIO 4: Diccionarios por comprensión
# ==============================================================================
# Tienes dos listas:
# nombres = ["Ana", "Luis", "María"]
# edades = [25, 30, 28]
# Crea un diccionario donde las claves sean los nombres y los valores las edades.
# Luego, crea otro diccionario que contenga solo las personas mayores de 26 años.

nombres: list = ["Ana", "Luis", "María"]
edades: list = [25, 30, 28]

# Tu código aquí:



# ==============================================================================
# EJERCICIO 5: Diccionarios anidados
# ==============================================================================
# Tienes el siguiente diccionario de estudiantes:
# estudiantes = {
#     "est1": {"nombre": "Ana", "notas": [85, 90, 88]},
#     "est2": {"nombre": "Luis", "notas": [78, 82, 80]},
#     "est3": {"nombre": "María", "notas": [92, 95, 90]}
# }
# Calcula e imprime:
# - El promedio de notas de cada estudiante
# - El nombre del estudiante con el promedio más alto

estudiantes: dict = {
    "est1": {"nombre": "Ana", "notas": [85, 90, 88]},
    "est2": {"nombre": "Luis", "notas": [78, 82, 80]},
    "est3": {"nombre": "María", "notas": [92, 95, 90]}
}

# Tu código aquí:



# ==============================================================================
# EJERCICIO 6: Operaciones básicas con sets
# ==============================================================================
# Tienes el set: colores = {"rojo", "verde", "azul"}
# Realiza en orden:
# 1. Agrega "amarillo"
# 2. Elimina "verde" usando remove()
# 3. Intenta eliminar "rosa" usando discard() (no debe dar error)
# 4. Verifica si "azul" está en el set
# Imprime el set final y el resultado de la verificación.

colores: set = {"rojo", "verde", "azul"}

# Tu código aquí:



# ==============================================================================
# EJERCICIO 7: Operaciones de conjuntos
# ==============================================================================
# Tienes dos sets de estudiantes inscritos en cursos:
# python_students = {"Ana", "Luis", "María", "Carlos"}
# javascript_students = {"Luis", "Sofía", "Carlos", "Pedro"}
# Calcula e imprime:
# - Estudiantes en ambos cursos (intersección)
# - Estudiantes en al menos un curso (unión)
# - Estudiantes solo en Python (diferencia)
# - Estudiantes en un curso pero no en ambos (diferencia simétrica)

python_students: set = {"Ana", "Luis", "María", "Carlos"}
javascript_students: set = {"Luis", "Sofía", "Carlos", "Pedro"}

# Tu código aquí:



# ==============================================================================
# EJERCICIO 8: Eliminación de duplicados con sets
# ==============================================================================
# Tienes la lista con duplicados: numeros = [5, 2, 9, 2, 5, 1, 9, 8, 5]
# Convierte a set para eliminar duplicados, luego convierte de vuelta a lista ordenada.
# Imprime ambas versiones.

numeros: list = [5, 2, 9, 2, 5, 1, 9, 8, 5]

# Tu código aquí:



# ==============================================================================
# EJERCICIO 9: Conteo de palabras con diccionario
# ==============================================================================
# Tienes el texto: "python es genial python es poderoso python es rapido"
# Crea un diccionario que cuente cuántas veces aparece cada palabra.
# Imprime el diccionario y la palabra más frecuente.

texto: str = "python es genial python es poderoso python es rapido"

# Tu código aquí:



# ==============================================================================
# EJERCICIO 10: FrozenSet y casos de uso
# ==============================================================================
# Crea dos frozensets: A = {1, 2, 3} y B = {3, 4, 5}
# Úsalos como claves en un diccionario donde el valor sea su intersección.
# Luego, crea un set que contenga ambos frozensets como elementos.
# Imprime ambos resultados.

# Tu código aquí:
