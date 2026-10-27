"""
SOLUCIONES - ESTRUCTURAS DE CONTROL EN PYTHON
==============================================
"""

# ==============================================================================
# EJERCICIO 1
# ==============================================================================
temperatura: float = 28.0

if temperatura < 15:
    print("Hace frío")
elif temperatura <= 25:
    print("Templado")
else:
    print("Hace calor")
# Salida: Hace calor


# ==============================================================================
# EJERCICIO 2
# ==============================================================================
edad: int = 17
tiene_permiso: bool = True

puede_conducir: bool = True if (edad >= 18 and tiene_permiso) else False
print(f"Puede conducir: {puede_conducir}")
# Salida: Puede conducir: False


# ==============================================================================
# EJERCICIO 3
# ==============================================================================
suma: int = 0
contador: int = 1

while contador <= 20:
    suma += contador
    contador += 1

print(f"Suma de los primeros 20 números: {suma}")
# Salida: Suma de los primeros 20 números: 210


# ==============================================================================
# EJERCICIO 4
# ==============================================================================
precios: list = [15.50, 23.99, 8.75, 42.00, 5.25]

total: float = 0
max_precio: float = precios[0]
min_precio: float = precios[0]

for precio in precios:
    total += precio
    if precio > max_precio:
        max_precio = precio
    if precio < min_precio:
        min_precio = precio

promedio: float = total / len(precios)

print(f"Total: ${total:.2f}")
print(f"Promedio: ${promedio:.2f}")
print(f"Más alto: ${max_precio:.2f}")
print(f"Más bajo: ${min_precio:.2f}")
# Salida: Total: $95.49, Promedio: $19.10, Más alto: $42.00, Más bajo: $5.25


# ==============================================================================
# EJERCICIO 5
# ==============================================================================
print("Números divisibles por 3 pero no por 5:")
for i in range(1, 51):
    if i % 3 == 0 and i % 5 != 0:
        print(i, end=" ")
print()
# Salida: 3 6 9 12 18 21 24 27 33 36 39 42 48


# ==============================================================================
# EJERCICIO 6
# ==============================================================================
estudiantes: list = ["Ana", "Luis", "María", "Carlos", "Sofía"]

for posicion, estudiante in enumerate(estudiantes, start=1):
    print(f"{posicion}. {estudiante}")
# Salida: 1. Ana, 2. Luis, 3. María, 4. Carlos, 5. Sofía


# ==============================================================================
# EJERCICIO 7
# ==============================================================================
productos: list = ["Laptop", "Mouse", "Teclado"]
precios: list = [999.99, 29.99, 79.99]
stock: list = [5, 20, 15]

print("Inventario:")
for producto, precio, cantidad in zip(productos, precios, stock):
    print(f"{producto}: ${precio:.2f} (stock: {cantidad})")

# Crear diccionario
inventario: dict = {producto: (precio, cantidad) 
                    for producto, precio, cantidad in zip(productos, precios, stock)}
print(f"\nDiccionario: {inventario}")
# Salida: Laptop: $999.99 (stock: 5), etc.
# Diccionario: {'Laptop': (999.99, 5), 'Mouse': (29.99, 20), 'Teclado': (79.99, 15)}


# ==============================================================================
# EJERCICIO 8
# ==============================================================================
print("Números procesados:")
for i in range(1, 31):
    if i % 7 == 0:
        print(f"\nBucle detenido en {i} (múltiplo de 7)")
        break
    if i % 2 == 0:
        continue
    print(i, end=" ")
# Salida: 1 3 5, Bucle detenido en 7


# ==============================================================================
# EJERCICIO 9
# ==============================================================================
contraseñas_validas: list = ["admin123", "python2024", "secreto"]
intento: str = "python2024"

for contraseña in contraseñas_validas:
    if contraseña == intento:
        print("Acceso concedido")
        break
else:
    print("Acceso denegado")
# Salida: Acceso concedido


# ==============================================================================
# EJERCICIO 10
# ==============================================================================
matriz: list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Suma total
suma_total: int = 0
for fila in matriz:
    for elemento in fila:
        suma_total += elemento
print(f"Suma total: {suma_total}")

# Suma diagonal principal
suma_diagonal: int = 0
for i in range(len(matriz)):
    suma_diagonal += matriz[i][i]
print(f"Suma diagonal: {suma_diagonal}")

# Matriz multiplicada por 2
matriz_doble: list = []
for fila in matriz:
    fila_doble: list = []
    for elemento in fila:
        fila_doble.append(elemento * 2)
    matriz_doble.append(fila_doble)

print("Matriz doble:")
for fila in matriz_doble:
    print(fila)
# Salida: Suma total: 45, Suma diagonal: 15
# Matriz doble: [[2, 4, 6], [8, 10, 12], [14, 16, 18]]
