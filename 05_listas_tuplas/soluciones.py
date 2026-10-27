"""
SOLUCIONES - LISTAS Y TUPLAS EN PYTHON
=======================================
"""

# ==============================================================================
# EJERCICIO 1
# ==============================================================================
dias: list = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

print("="*60)
print("EJERCICIO 1: Creación y acceso")
print("="*60)
print(f"\nPrimer día: {dias[0]}")
print(f"Último día: {dias[-1]}")
print(f"Días laborales: {dias[0:5]}")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 2
# ==============================================================================
numeros: list = [10, 20, 40, 50]

print("\nEJERCICIO 2: Métodos de modificación")
print("="*60)

numeros.insert(2, 30)
print(f"1. Tras insert(2, 30): {numeros}")

numeros.append(60)
print(f"2. Tras append(60): {numeros}")

numeros.remove(10)
print(f"3. Tras remove(10): {numeros}")

numeros.reverse()
print(f"4. Tras reverse(): {numeros}")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 3
# ==============================================================================
informacion: tuple = ("Carlos", 28, "Desarrollador", "Madrid", "Python")

print("\nEJERCICIO 3: Desempaquetado de tuplas")
print("="*60)

nombre, edad, *resto = informacion

print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Resto: {resto} (tipo: {type(resto)})")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 4
# ==============================================================================
puntuaciones: list = [85, 92, 78, 90, 88, 95]

print("\nEJERCICIO 4: Ordenamiento y funciones integradas")
print("="*60)

print(f"Puntuación más alta: {max(puntuaciones)}")
print(f"Puntuación más baja: {min(puntuaciones)}")

promedio: float = sum(puntuaciones) / len(puntuaciones)
print(f"Promedio: {promedio:.2f}")

ordenada_mayor_a_menor: list = sorted(puntuaciones, reverse=True)
print(f"Ordenada (original intacta): {ordenada_mayor_a_menor}")
print(f"Lista original: {puntuaciones}")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 5
# ==============================================================================
palabras: list = ["python", "es", "genial", "y", "poderoso"]

print("\nEJERCICIO 5: Listas por comprensión")
print("="*60)

filtradas_y_mayusculas: list = [palabra.upper() for palabra in palabras if len(palabra) > 3]

print(f"Lista original: {palabras}")
print(f"Lista procesada: {filtradas_y_mayusculas}")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 6
# ==============================================================================
lista_a: list = [1, 2, 3, 4]
lista_b: list = [3, 4, 5, 6]

print("\nEJERCICIO 6: Operaciones entre listas")
print("="*60)

concatenada: list = lista_a + lista_b
print(f"Concatenación: {concatenada}")

# Unión de elementos únicos
unicos: list = sorted(list(set(lista_a + lista_b)))
print(f"Elementos únicos ordenados: {unicos}")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 7
# ==============================================================================
matriz: list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("\nEJERCICIO 7: Matrices (listas anidadas)")
print("="*60)

suma_segunda_fila: int = sum(matriz[1])
print(f"Suma de la segunda fila: {suma_segunda_fila}")

tercera_columna: list = [fila[2] for fila in matriz]
print(f"Elementos de la tercera columna: {tercera_columna}")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 8
# ==============================================================================
datos: tuple = (100, 200, [300, 400])

print("\nEJERCICIO 8: Inmutabilidad de tuplas")
print("="*60)

# Explicación: La tupla en sí es inmutable (no podemos reasignar datos[2] a otra cosa),
# pero el objeto lista que está en la posición 2 SÍ es mutable.
# Por lo tanto, podemos modificar el contenido de esa lista interna.
datos[2].append(500)

print(f"Tupla tras modificar la lista interna: {datos}")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 9
# ==============================================================================
con_duplicados: list = [5, 2, 9, 2, 5, 1, 9, 8]

print("\nEJERCICIO 9: Eliminación de duplicados manteniendo orden")
print("="*60)

# Método 1: Usando dict (mantiene orden de inserción desde Python 3.7)
sin_duplicados_dict: list = list(dict.fromkeys(con_duplicados))
print(f"Usando dict.fromkeys: {sin_duplicados_dict}")

# Método 2: Usando bucle y lista auxiliar (más explícito para principiantes)
sin_duplicados_bucle: list = []
for elemento in con_duplicados:
    if elemento not in sin_duplicados_bucle:
        sin_duplicados_bucle.append(elemento)

print(f"Usando bucle auxiliar: {sin_duplicados_bucle}")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 10
# ==============================================================================
print("\nEJERCICIO 10: Simulación de carrito de compras")
print("="*60)

carrito: list = []

carrito.append(("Laptop", 999))
carrito.append(("Mouse", 25))
print(f"1. Tras agregar Laptop y Mouse: {carrito}")

carrito.append(("Teclado", 45))
print(f"2. Tras agregar Teclado: {carrito}")

carrito.remove(("Mouse", 25))
print(f"3. Tras eliminar Mouse: {carrito}")

total_a_pagar: float = sum(item[1] for item in carrito)
print(f"4. Total a pagar: ${total_a_pagar:.2f}")
print("\n" + "="*60)
