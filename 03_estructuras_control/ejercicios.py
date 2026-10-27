"""
EJERCICIOS - ESTRUCTURAS DE CONTROL EN PYTHON
==============================================
Resuelve cada ejercicio. No mires las soluciones hasta terminar.
"""

# ==============================================================================
# EJERCICIO 1: Condicional simple
# ==============================================================================
# Tienes una variable 'temperatura' con valor 28.
# Imprime:
# - "Hace frío" si es menor a 15
# - "Templado" si está entre 15 y 25 (inclusive)
# - "Hace calor" si es mayor a 25

temperatura: float = 28.0

# Tu código aquí:



# ==============================================================================
# EJERCICIO 2: Operador ternario
# ==============================================================================
# Tienes dos variables: 'edad' = 17 y 'tiene_permiso' = True
# Crea una variable 'puede_conducir' que sea True solo si es mayor o igual a 18
# Y tiene permiso. Usa operador ternario anidado o lógico.
# Imprime el resultado.

edad: int = 17
tiene_permiso: bool = True

# Tu código aquí:



# ==============================================================================
# EJERCICIO 3: While con contador
# ==============================================================================
# Usa un bucle while para calcular la suma de los primeros 20 números naturales.
# Imprime el resultado final.

# Tu código aquí:



# ==============================================================================
# EJERCICIO 4: For con lista
# ==============================================================================
# Tienes una lista de precios: [15.50, 23.99, 8.75, 42.00, 5.25]
# Calcula e imprime:
# - El precio total
# - El precio promedio
# - El precio más alto y más bajo (sin usar max() ni min())

precios: list = [15.50, 23.99, 8.75, 42.00, 5.25]

# Tu código aquí:



# ==============================================================================
# EJERCICIO 5: Range y filtro
# ==============================================================================
# Usa range y un bucle for para imprimir todos los números del 1 al 50
# que sean divisibles por 3 pero NO por 5.

# Tu código aquí:



# ==============================================================================
# EJERCICIO 6: Enumerate
# ==============================================================================
# Tienes una lista de estudiantes: ["Ana", "Luis", "María", "Carlos", "Sofía"]
# Usa enumerate para imprimir cada estudiante con su posición (iniciando en 1).
# Formato: "1. Ana, 2. Luis, ..."

estudiantes: list = ["Ana", "Luis", "María", "Carlos", "Sofía"]

# Tu código aquí:



# ==============================================================================
# EJERCICIO 7: Zip
# ==============================================================================
# Tienes tres listas:
# - productos: ["Laptop", "Mouse", "Teclado"]
# - precios: [999.99, 29.99, 79.99]
# - stock: [5, 20, 15]
# Usa zip para imprimir cada producto con su precio y stock.
# Luego crea un diccionario donde las claves sean productos y los valores
# sean tuplas (precio, stock).

productos: list = ["Laptop", "Mouse", "Teclado"]
precios: list = [999.99, 29.99, 79.99]
stock: list = [5, 20, 15]

# Tu código aquí:



# ==============================================================================
# EJERCICIO 8: Break y continue
# ==============================================================================
# Itera sobre los números del 1 al 30:
# - Si el número es múltiplo de 7, usa break para detener el bucle
# - Si el número es par, usa continue para saltarlo
# - Imprime los números que pasen ambos filtros
# Al final, imprime un mensaje indicando dónde se detuvo el bucle.

# Tu código aquí:



# ==============================================================================
# EJERCICIO 9: Else en bucles
# ==============================================================================
# Tienes una lista de contraseñas válidas: ["admin123", "python2024", "secreto"]
# Pide al usuario una contraseña (simula con una variable).
# Usa un bucle for con else para verificar si está en la lista.
# Si la encuentra, imprime "Acceso concedido" y usa break.
# Si el bucle termina sin encontrarla, el else debe imprimir "Acceso denegado".

contraseñas_validas: list = ["admin123", "python2024", "secreto"]
intento: str = "python2024"  # Cambia esto para probar

# Tu código aquí:



# ==============================================================================
# EJERCICIO 10: Bucles anidados y matrices
# ==============================================================================
# Tienes una matriz 3x3:
# matriz = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# Calcula e imprime:
# - La suma de todos los elementos
# - La suma de la diagonal principal (1, 5, 9)
# - Una nueva matriz donde cada elemento esté multiplicado por 2

matriz: list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Tu código aquí:
