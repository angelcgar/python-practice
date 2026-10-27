"""
EJERCICIOS - LISTAS Y TUPLAS EN PYTHON
=======================================
Resuelve cada ejercicio. No mires las soluciones hasta terminar.
"""

# ==============================================================================
# EJERCICIO 1: Creación y acceso
# ==============================================================================
# Crea una lista llamada 'dias' con los 7 días de la semana.
# Imprime:
# - El primer día
# - El último día (usando índice negativo)
# - Una sublista con los días de la semana laboral (lunes a viernes)

# Tu código aquí:



# ==============================================================================
# EJERCICIO 2: Métodos de modificación
# ==============================================================================
# Tienes la lista: numeros = [10, 20, 40, 50]
# Realiza las siguientes operaciones en orden e imprime la lista tras cada una:
# 1. Inserta el número 30 en la posición correcta (índice 2).
# 2. Agrega el número 60 al final.
# 3. Elimina el número 10.
# 4. Invierte la lista.

numeros: list = [10, 20, 40, 50]

# Tu código aquí:



# ==============================================================================
# EJERCICIO 3: Desempaquetado de tuplas
# ==============================================================================
# Tienes la tupla: informacion = ("Carlos", 28, "Desarrollador", "Madrid", "Python")
# Desempaqueta la tupla en 3 variables: 'nombre', 'edad', y 'resto' (que debe ser una lista con los 3 elementos restantes).
# Imprime cada variable.

informacion: tuple = ("Carlos", 28, "Desarrollador", " Madrid", "Python")

# Tu código aquí:



# ==============================================================================
# EJERCICIO 4: Ordenamiento y funciones integradas
# ==============================================================================
# Tienes la lista de puntuaciones: [85, 92, 78, 90, 88, 95]
# Imprime:
# - La puntuación más alta y la más baja.
# - El promedio de las puntuaciones.
# - La lista ordenada de mayor a menor (sin modificar la original).

puntuaciones: list = [85, 92, 78, 90, 88, 95]

# Tu código aquí:



# ==============================================================================
# EJERCICIO 5: Listas por comprensión
# ==============================================================================
# Tienes la lista de palabras: ["python", "es", "genial", "y", "poderoso"]
# Crea una nueva lista que contenga solo las palabras con más de 3 caracteres,
# pero en mayúsculas.
# Imprime la lista resultante.

palabras: list = ["python", "es", "genial", "y", "poderoso"]

# Tu código aquí:



# ==============================================================================
# EJERCICIO 6: Operaciones entre listas
# ==============================================================================
# Tienes dos listas:
# lista_a = [1, 2, 3, 4]
# lista_b = [3, 4, 5, 6]
# Crea e imprime:
# - Una lista con la concatenación de ambas.
# - Una lista con los elementos únicos de ambas (pista: usa set como paso intermedio, luego conviértelo a lista y ordénalo).

lista_a: list = [1, 2, 3, 4]
lista_b: list = [3, 4, 5, 6]

# Tu código aquí:



# ==============================================================================
# EJERCICIO 7: Matrices (listas anidadas)
# ==============================================================================
# Tienes la matriz 3x3:
# matriz = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# Calcula e imprime:
# - La suma de la segunda fila (índice 1).
# - Una lista con todos los elementos de la tercera columna (índice 2).

matriz: list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Tu código aquí:



# ==============================================================================
# EJERCICIO 8: Inmutabilidad de tuplas
# ==============================================================================
# Tienes la tupla: datos = (100, 200, [300, 400])
# Intenta explicar en un comentario por qué la siguiente línea funciona sin errores:
# datos[2].append(500)
# Luego, imprime la tupla 'datos' para verificar el resultado.

datos: tuple = (100, 200, [300, 400])

# Tu código aquí:



# ==============================================================================
# EJERCICIO 9: Eliminación de duplicados manteniendo orden
# ==============================================================================
# Tienes la lista con duplicados: [5, 2, 9, 2, 5, 1, 9, 8]
# Crea una nueva lista que elimine los duplicados pero mantenga el orden
# de la primera aparición de cada elemento.
# (Pista: puedes usar un bucle for y una lista auxiliar, o un dict desde Python 3.7+).

con_duplicados: list = [5, 2, 9, 2, 5, 1, 9, 8]

# Tu código aquí:



# ==============================================================================
# EJERCICIO 10: Simulación de carrito de compras
# ==============================================================================
# Crea una lista vacía 'carrito'.
# Simula las siguientes acciones imprimiendo el estado del carrito en cada paso:
# 1. Agrega "Laptop" ($999) y "Mouse" ($25) como tuplas (producto, precio).
# 2. Agrega "Teclado" ($45) usando append.
# 3. Elimina el "Mouse" usando remove.
# 4. Calcula e imprime el total a pagar sumando los precios.

# Tu código aquí:
