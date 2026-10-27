"""
EJERCICIOS - OPERADORES EN PYTHON
==================================
Resuelve cada ejercicio. No mires las soluciones hasta terminar.
"""

# ==============================================================================
# EJERCICIO 1: Operadores aritméticos básicos
# ==============================================================================
# Tienes dos números: a = 25, b = 7
# Calcula e imprime: suma, resta, multiplicación, división, división entera,
# módulo y potencia (a elevado a b).
# Imprime cada resultado con su tipo de dato.

a: int = 25
b: int = 7

# Tu código aquí:



# ==============================================================================
# EJERCICIO 2: Conversión de tiempo
# ==============================================================================
# Tienes un total de 7380 segundos.
# Convierte ese valor a horas, minutos y segundos usando // y %.
# Formato esperado: "X horas, Y minutos, Z segundos"

total_segundos: int = 7380

# Tu código aquí:



# ==============================================================================
# EJERCICIO 3: Operadores de comparación y lógicos
# ==============================================================================
# Tienes la edad de 3 personas: persona1 = 17, persona2 = 25, persona3 = 30
# Crea una variable 'pueden_entrar' que sea True si TODAS son mayores o iguales a 18.
# Crea otra variable 'alguno_mayor' que sea True si al menos UNA es mayor a 25.
# Imprime ambas variables.

persona1: int = 17
persona2: int = 25
persona3: int = 30

# Tu código aquí:



# ==============================================================================
# EJERCICIO 4: Operadores de asignación compuesta
# ==============================================================================
# Inicia una variable 'saldo' en 1000.
# Aplica en orden:
# - Suma 500
# - Resta 200
# - Multiplica por 2
# - Divide entre 4 (división entera)
# - Eleva al cuadrado
# Imprime el saldo final.

saldo: int = 1000

# Tu código aquí:



# ==============================================================================
# EJERCICIO 5: Operadores de identidad
# ==============================================================================
# Crea dos listas con los mismos valores: [1, 2, 3]
# Crea una tercera variable que apunte a la primera lista.
# Verifica con 'is' y '==' qué relaciones existen entre las tres.
# Imprime los resultados y los id() de cada lista.

# Tu código aquí:



# ==============================================================================
# EJERCICIO 6: Operadores de pertenencia
# ==============================================================================
# Tienes:
# - un string: "Desarrollo Web con Python"
# - una lista de lenguajes: ["Python", "JavaScript", "Go", "Rust"]
# - un diccionario de versiones: {"Python": "3.11", "JS": "ES2024"}
# Verifica e imprime:
# - Si "Python" está en el string
# - Si "Java" NO está en la lista
# - Si "Python" es clave del diccionario
# - Si "3.11" NO está en el diccionario

texto: str = "Desarrollo Web con Python"
lenguajes: list = ["Python", "JavaScript", "Go", "Rust"]
versiones: dict = {"Python": "3.11", "JS": "ES2024"}

# Tu código aquí:



# ==============================================================================
# EJERCICIO 7: Operadores bit a bit
# ==============================================================================
# Tienes dos números: x = 60, y = 13
# Calcula e imprime: AND, OR, XOR, NOT de x, desplazamiento izquierda de x por 2,
# desplazamiento derecha de x por 2.
# Muestra también la representación binaria de cada resultado.

x: int = 60
y: int = 13

# Tu código aquí:



# ==============================================================================
# EJERCICIO 8: Operador walrus
# ==============================================================================
# Tienes una lista de números: [5, 12, 8, 20, 3, 15]
# Usa el operador walrus para:
# - Filtrar los números mayores a 10 en una lista
# - Si la lista filtrada tiene más de 2 elementos, imprime su suma
# Hazlo en una sola expresión if con walrus.

numeros: list = [5, 12, 8, 20, 3, 15]

# Tu código aquí:



# ==============================================================================
# EJERCICIO 9: Operadores en strings
# ==============================================================================
# Tienes: palabra = "Python"
# - Concatena " es genial" al final
# - Repite la palabra 4 veces separada por guiones (usa concatenación y repetición)
# - Verifica si "Py" está en la palabra y si "Java" no está
# Imprime cada resultado.

palabra: str = "Python"

# Tu código aquí:



# ==============================================================================
# EJERCICIO 10: Precedencia de operadores
# ==============================================================================
# Sin ejecutar, predice el resultado de estas expresiones. Luego verifica.
# - expresion_1 = 2 + 3 * 4
# - expresion_2 = (2 + 3) * 4
# - expresion_3 = 2 ** 3 ** 2  (pista: ** es asociativo por la derecha)
# - expresion_4 = 10 - 2 * 3 + 1
# - expresion_5 = True or False and False
# Imprime cada resultado.

# Tu código aquí:
