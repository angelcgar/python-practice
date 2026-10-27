"""
SOLUCIONES - DICCIONARIOS Y SETS EN PYTHON
===========================================
"""

# ==============================================================================
# EJERCICIO 1
# ==============================================================================
libro: dict = {
    "titulo": "Python Crash Course",
    "autor": "Eric Matthes",
    "año": 2019,
    "genero": "Programación"
}

print("="*60)
print("EJERCICIO 1: Creación y acceso")
print("="*60)

print(f"\nTítulo: {libro['titulo']}")
print(f"Autor: {libro.get('autor')}")
print(f"ISBN: {libro.get('isbn', 'No disponible')}")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 2
# ==============================================================================
estudiante: dict = {"nombre": "Luis", "edad": 20, "cursos": ["Python"]}

print("\nEJERCICIO 2: Modificación y eliminación")
print("="*60)

estudiante["promedio"] = 85.5
print(f"1. Tras agregar 'promedio': {estudiante}")

estudiante.update({"edad": 21})
print(f"2. Tras update(): {estudiante}")

estudiante["cursos"].append("JavaScript")
print(f"3. Tras agregar curso: {estudiante}")

edad_eliminada = estudiante.pop("edad")
print(f"4. Tras pop('edad'): {estudiante} (retornó: {edad_eliminada})")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 3
# ==============================================================================
productos: dict = {"Laptop": 999, "Mouse": 25, "Teclado": 75, "Monitor": 300, "Webcam": 60}

print("\nEJERCICIO 3: Iteración y filtrado")
print("="*60)

productos_caros: list = [nombre for nombre, precio in productos.items() if precio > 50]
print(f"\nProductos con precio > 50: {productos_caros}")

precio_total: float = sum(productos.values())
print(f"Precio total: ${precio_total:.2f}")

producto_mas_caro: str = max(productos, key=productos.get)
producto_mas_barato: str = min(productos, key=productos.get)
print(f"Más caro: {producto_mas_caro} (${productos[producto_mas_caro]})")
print(f"Más barato: {producto_mas_barato} (${productos[producto_mas_barato]})")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 4
# ==============================================================================
nombres: list = ["Ana", "Luis", "María"]
edades: list = [25, 30, 28]

print("\nEJERCICIO 4: Diccionarios por comprensión")
print("="*60)

personas: dict = {nombre: edad for nombre, edad in zip(nombres, edades)}
print(f"\nDiccionario completo: {personas}")

mayores_de_26: dict = {k: v for k, v in personas.items() if v > 26}
print(f"Mayores de 26: {mayores_de_26}")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 5
# ==============================================================================
estudiantes: dict = {
    "est1": {"nombre": "Ana", "notas": [85, 90, 88]},
    "est2": {"nombre": "Luis", "notas": [78, 82, 80]},
    "est3": {"nombre": "María", "notas": [92, 95, 90]}
}

print("\nEJERCICIO 5: Diccionarios anidados")
print("="*60)

promedios: dict = {}
for id_est, datos in estudiantes.items():
    promedio = sum(datos["notas"]) / len(datos["notas"])
    promedios[datos["nombre"]] = promedio
    print(f"{datos['nombre']}: promedio {promedio:.2f}")

mejor_estudiante: str = max(promedios, key=promedios.get)
print(f"\nMejor estudiante: {mejor_estudiante} con {promedios[mejor_estudiante]:.2f}")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 6
# ==============================================================================
colores: set = {"rojo", "verde", "azul"}

print("\nEJERCICIO 6: Operaciones básicas con sets")
print("="*60)

colores.add("amarillo")
print(f"\n1. Tras add('amarillo'): {colores}")

colores.remove("verde")
print(f"2. Tras remove('verde'): {colores}")

colores.discard("rosa")
print(f"3. Tras discard('rosa'): {colores}")

esta_azul: bool = "azul" in colores
print(f"4. 'azul' en colores: {esta_azul}")
print(f"\nSet final: {colores}")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 7
# ==============================================================================
python_students: set = {"Ana", "Luis", "María", "Carlos"}
javascript_students: set = {"Luis", "Sofía", "Carlos", "Pedro"}

print("\nEJERCICIO 7: Operaciones de conjuntos")
print("="*60)

ambos: set = python_students & javascript_students
print(f"\nEn ambos cursos: {ambos}")

al_menos_uno: set = python_students | javascript_students
print(f"En al menos un curso: {al_menos_uno}")

solo_python: set = python_students - javascript_students
print(f"Solo en Python: {solo_python}")

solo_uno: set = python_students ^ javascript_students
print(f"En uno pero no en ambos: {solo_uno}")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 8
# ==============================================================================
numeros: list = [5, 2, 9, 2, 5, 1, 9, 8, 5]

print("\nEJERCICIO 8: Eliminación de duplicados con sets")
print("="*60)

print(f"\nLista original: {numeros}")

sin_duplicados: list = sorted(list(set(numeros)))
print(f"Lista sin duplicados (ordenada): {sin_duplicados}")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 9
# ==============================================================================
texto: str = "python es genial python es poderoso python es rapido"

print("\nEJERCICIO 9: Conteo de palabras con diccionario")
print("="*60)

palabras: list = texto.split()
conteo: dict = {}

for palabra in palabras:
    conteo[palabra] = conteo.get(palabra, 0) + 1

print(f"\nConteo de palabras: {conteo}")

palabra_mas_frecuente: str = max(conteo, key=conteo.get)
print(f"Palabra más frecuente: '{palabra_mas_frecuente}' ({conteo[palabra_mas_frecuente]} veces)")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 10
# ==============================================================================
print("\nEJERCICIO 10: FrozenSet y casos de uso")
print("="*60)

A: frozenset = frozenset([1, 2, 3])
B: frozenset = frozenset([3, 4, 5])

interseccion: set = A & B
diccionario: dict = {A: list(interseccion), B: list(interseccion)}
print(f"\nDiccionario con frozensets como claves: {diccionario}")

set_de_frozensets: set = {A, B}
print(f"Set de frozensets: {set_de_frozensets}")
print("\n" + "="*60)
