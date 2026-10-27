"""
ESTRUCTURAS DE CONTROL EN PYTHON - GUÍA COMPLETA
=================================================
Condicionales y bucles, explicados con anotaciones de tipo.
"""

# ==============================================================================
# 1. CONDICIONAL IF / ELIF / ELSE
# ==============================================================================
# Ejecuta bloques de código según condiciones booleanas.

edad: int = 20

if edad < 18:
    print("Menor de edad")
elif edad < 65:
    print("Adulto")
else:
    print("Adulto mayor")
# Salida: Adulto


# Múltiples condiciones con operadores lógicos
temperatura: float = 22.5
esta_lloviendo: bool = False

if temperatura > 20 and not esta_lloviendo:
    print("Buen día para salir")
elif temperatura <= 10 or esta_lloviendo:
    print("Mejor quedarse en casa")
else:
    print("Día normal")
# Salida: Buen día para salir


# If anidados
nota: int = 85

if nota >= 60:
    if nota >= 90:
        print("Excelente")
    elif nota >= 75:
        print("Muy bien")
    else:
        print("Aprobado")
else:
    print("Reprobado")
# Salida: Muy bien


# ==============================================================================
# 2. OPERADOR TERNARIO (IF EN UNA LÍNEA)
# ==============================================================================
# Sintaxis: valor_si_verdadero if condicion else valor_si_falso

edad: int = 20
estado: str = "Mayor" if edad >= 18 else "Menor"
print(f"Estado: {estado}")
# Salida: Estado: Mayor

# Útil para asignaciones condicionales simples
numero: int = -5
valor_absoluto: int = numero if numero >= 0 else -numero
print(f"Valor absoluto: {valor_absoluto}")
# Salida: Valor absoluto: 5


# ==============================================================================
# 3. BUCLE WHILE
# ==============================================================================
# Ejecuta un bloque mientras la condición sea True.

contador: int = 1
while contador <= 5:
    print(f"Contador: {contador}")
    contador += 1
# Salida: Contador: 1, 2, 3, 4, 5


# While con condición compuesta
suma: int = 0
numero: int = 1
while suma < 50:
    suma += numero
    numero += 1

print(f"Suma final: {suma}, con {numero - 1} números")
# Salida: Suma final: 55, con 10 números


# ==============================================================================
# 4. BUCLE FOR
# ==============================================================================
# Itera sobre cualquier secuencia iterable (list, tuple, str, range, dict, set).

# Iterando sobre una lista
frutas: list = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print(f"Fruta: {fruta}")
# Salida: Fruta: manzana, banana, naranja


# Iterando sobre un string
palabra: str = "Python"
for letra in palabra:
    print(letra, end=" ")
print()  # Salto de línea
# Salida: P y t h o n


# Iterando sobre un diccionario (claves por defecto)
persona: dict = {"nombre": "Ana", "edad": 30, "ciudad": "Madrid"}
for clave in persona:
    print(f"{clave}: {persona[clave]}")
# Salida: nombre: Ana, edad: 30, ciudad: Madrid


# Iterando sobre claves y valores
for clave, valor in persona.items():
    print(f"{clave} = {valor}")
# Salida: nombre = Ana, edad = 30, ciudad = Madrid


# Iterando sobre un set
numeros: set = {1, 2, 3, 4, 5}
for num in numeros:
    print(num, end=" ")
print()
# Salida: 1 2 3 4 5 (orden no garantizado)


# ==============================================================================
# 5. FUNCIÓN RANGE
# ==============================================================================
# Genera secuencias de números enteros. Muy usada con for.

# range(fin): de 0 a fin-1
for i in range(5):
    print(i, end=" ")
print()
# Salida: 0 1 2 3 4


# range(inicio, fin): de inicio a fin-1
for i in range(2, 7):
    print(i, end=" ")
print()
# Salida: 2 3 4 5 6


# range(inicio, fin, paso): con incremento personalizado
for i in range(0, 20, 3):
    print(i, end=" ")
print()
# Salida: 0 3 6 9 12 15 18


# Range en reversa
for i in range(10, 0, -2):
    print(i, end=" ")
print()
# Salida: 10 8 6 4 2


# ==============================================================================
# 6. FUNCIÓN ENUMERATE
# ==============================================================================
# Itera sobre una secuencia obteniendo índice y valor simultáneamente.

nombres: list = ["Ana", "Luis", "María", "Carlos"]

for indice, nombre in enumerate(nombres):
    print(f"Índice {indice}: {nombre}")
# Salida: Índice 0: Ana, 1: Luis, 2: María, 3: Carlos


# Enumerate con inicio personalizado
for indice, nombre in enumerate(nombres, start=1):
    print(f"Posición {indice}: {nombre}")
# Salida: Posición 1: Ana, 2: Luis, 3: María, 4: Carlos


# ==============================================================================
# 7. FUNCIÓN ZIP
# ==============================================================================
# Combina múltiples iterables en tuplas. Se detiene en el iterable más corto.

nombres: list = ["Ana", "Luis", "María"]
edades: list = [25, 30, 28]
ciudades: list = ["Madrid", "Barcelona", "Valencia"]

for nombre, edad, ciudad in zip(nombres, edades, ciudades):
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")
# Salida: Ana tiene 25 años..., Luis tiene 30..., María tiene 28...


# Zip para crear diccionarios
llaves: list = ["a", "b", "c"]
valores: list = [1, 2, 3]
diccionario: dict = dict(zip(llaves, valores))
print(f"Diccionario: {diccionario}")
# Salida: Diccionario: {'a': 1, 'b': 2, 'c': 3}


# ==============================================================================
# 8. BREAK, CONTINUE Y PASS
# ==============================================================================

# break: sale del bucle inmediatamente
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
print()
# Salida: 0 1 2 3 4


# continue: salta a la siguiente iteración
for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()
# Salida: 1 3 5 7 9


# pass: no hace nada, marcador de posición
for i in range(5):
    pass  # Útil para bucles vacíos o código pendiente

# Ejemplo real: estructura pendiente de implementar
def funcion_pendiente():
    pass  # TODO: implementar


# ==============================================================================
# 9. ELSE EN BUCLES
# ==============================================================================
# Python permite else en for y while. Se ejecuta si el bucle termina normalmente
# (sin break).

# Buscar un elemento
numeros: list = [4, 6, 8, 10, 12]
buscado: int = 7

for num in numeros:
    if num == buscado:
        print(f"Encontrado: {buscado}")
        break
else:
    print(f"No se encontró {buscado} en la lista")
# Salida: No se encontró 7 en la lista


# While con else
contador: int = 0
while contador < 5:
    contador += 1
else:
    print("Bucle completado sin break")
# Salida: Bucle completado sin break


# ==============================================================================
# 10. BUCLES ANIDADOS
# ==============================================================================

# Tabla de multiplicar
for i in range(1, 4):
    for j in range(1, 6):
        print(f"{i}x{j}={i*j}", end="\t")
    print()
# Salida:
# 1x1=1   1x2=2   1x3=3   1x4=4   1x5=5
# 2x1=2   2x2=4   2x3=6   2x4=8   2x5=10
# 3x1=3   3x2=6   3x3=9   3x4=12  3x5=15


# Matriz (lista de listas)
matriz: list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()
# Salida:
# 1 2 3
# 4 5 6
# 7 8 9


# ==============================================================================
# 11. COMPRENSIONES (INTRODUCCIÓN)
# ==============================================================================
# Forma concisa de crear listas, diccionarios y sets con bucles.

# Lista por comprensión
cuadrados: list = [x**2 for x in range(1, 6)]
print(f"Cuadrados: {cuadrados}")
# Salida: Cuadrados: [1, 4, 9, 16, 25]


# Con condición (filtro)
pares: list = [x for x in range(10) if x % 2 == 0]
print(f"Pares: {pares}")
# Salida: Pares: [0, 2, 4, 6, 8]


# Set por comprensión
vocales_unicas: set = {c.lower() for c in "Hola Mundo"}
print(f"Vocales únicas: {vocales_unicas}")
# Salida: {'a', 'o', 'u', 'h', 'l', 'm', 'n', 'd'} (todas las letras únicas)


# Diccionario por comprensión
tabla_cuadrados: dict = {x: x**2 for x in range(1, 6)}
print(f"Tabla: {tabla_cuadrados}")
# Salida: Tabla: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# ==============================================================================
# RESUMEN
# ==============================================================================
print("\n" + "="*60)
print("ESTRUCTURAS DE CONTROL EN PYTHON")
print("="*60)
print("Condicionales: if, elif, else, operador ternario")
print("Bucles: while, for")
print("Herramientas: range, enumerate, zip")
print("Control de flujo: break, continue, pass")
print("Características: else en bucles, bucles anidados")
print("Comprensiones: list, set, dict")
print("="*60)
