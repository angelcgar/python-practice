"""
DICCIONARIOS Y SETS EN PYTHON - GUÍA COMPLETA
==============================================
Estructuras de datos no ordenadas: mapeos y conjuntos.
"""

# ==============================================================================
# 1. CREACIÓN DE DICCIONARIOS
# ==============================================================================
print("="*60)
print("1. CREACIÓN DE DICCIONARIOS")
print("="*60)

# Literal con llaves {}
persona: dict = {"nombre": "Ana", "edad": 30, "ciudad": "Madrid"}

# Diccionario vacío
vacio: dict = {}

# Constructor dict() con pares clave-valor
desde_pares: dict = dict([("a", 1), ("b", 2), ("c", 3)])

# Constructor con kwargs
desde_kwargs: dict = dict(x=10, y=20, z=30)

# Claves pueden ser de cualquier tipo inmutable
mixto: dict = {1: "uno", "dos": 2, 3.0: "tres", True: "verdadero"}

print(f"\nLiteral: {persona}")
print(f"Desde pares: {desde_pares}")
print(f"Desde kwargs: {desde_kwargs}")
print(f"Claves mixtas: {mixto}")
print("\n" + "-"*60)


# ==============================================================================
# 2. ACCESO A VALORES
# ==============================================================================
print("\n2. ACCESO A VALORES")
print("="*60)

persona: dict = {"nombre": "Ana", "edad": 30, "ciudad": "Madrid"}

# Acceso directo con [] (lanza KeyError si no existe)
print(f"\nAcceso con []:")
print(f"  persona['nombre']: {persona['nombre']}")

# Acceso con get() (retorna None o valor por defecto si no existe)
print(f"\nAcceso con get():")
print(f"  persona.get('edad'): {persona.get('edad')}")
print(f"  persona.get('telefono'): {persona.get('telefono')}")
print(f"  persona.get('telefono', 'No disponible'): {persona.get('telefono', 'No disponible')}")

# Obtener todas las claves, valores o pares
print(f"\nVistas del diccionario:")
print(f"  keys(): {list(persona.keys())}")
print(f"  values(): {list(persona.values())}")
print(f"  items(): {list(persona.items())}")
print("\n" + "-"*60)


# ==============================================================================
# 3. MODIFICACIÓN DE DICCIONARIOS
# ==============================================================================
print("\n3. MODIFICACIÓN DE DICCIONARIOS")
print("="*60)

persona: dict = {"nombre": "Ana", "edad": 30}

print(f"\nOriginal: {persona}")

# Agregar o modificar con []
persona["ciudad"] = "Madrid"
persona["edad"] = 31
print(f"Tras agregar 'ciudad' y modificar 'edad': {persona}")

# update() agrega/modifica múltiples claves a la vez
persona.update({"profesion": "Desarrolladora", "edad": 32})
print(f"Tras update(): {persona}")

# setdefault() asigna valor solo si la clave no existe
persona.setdefault("pais", "España")
persona.setdefault("nombre", "Desconocido")  # No cambia, ya existe
print(f"Tras setdefault(): {persona}")
print("\n" + "-"*60)


# ==============================================================================
# 4. ELIMINACIÓN EN DICCIONARIOS
# ==============================================================================
print("\n4. ELIMINACIÓN EN DICCIONARIOS")
print("="*60)

persona: dict = {"nombre": "Ana", "edad": 30, "ciudad": "Madrid", "pais": "España"}

print(f"\nOriginal: {persona}")

# pop() elimina y retorna el valor (requiere clave)
edad_eliminada = persona.pop("edad")
print(f"Tras pop('edad'): {persona} (retornó: {edad_eliminada})")

# pop() con valor por defecto (no lanza error si no existe)
resultado = persona.pop("telefono", "No existía")
print(f"pop('telefono', 'No existía'): {resultado}")

# popitem() elimina el último par insertado (LIFO)
ultimo = persona.popitem()
print(f"Tras popitem(): {persona} (retornó: {ultimo})")

# del elimina por clave
del persona["pais"]
print(f"Tras del persona['pais']: {persona}")

# clear() vacía el diccionario
persona.clear()
print(f"Tras clear(): {persona}")
print("\n" + "-"*60)


# ==============================================================================
# 5. ITERACIÓN SOBRE DICCIONARIOS
# ==============================================================================
print("\n5. ITERACIÓN SOBRE DICCIONARIOS")
print("="*60)

precios: dict = {"Laptop": 999, "Mouse": 25, "Teclado": 75}

print(f"\nDiccionario: {precios}\n")

print("Iterar sobre claves:")
for clave in precios:
    print(f"  {clave}")

print("\nIterar sobre valores:")
for valor in precios.values():
    print(f"  {valor}")

print("\nIterar sobre pares clave-valor:")
for clave, valor in precios.items():
    print(f"  {clave}: {valor}")
print("\n" + "-"*60)


# ==============================================================================
# 6. DICCIONARIOS POR COMPRENSIÓN
# ==============================================================================
print("\n6. DICCIONARIOS POR COMPRENSIÓN")
print("="*60)

# Sintaxis: {clave: valor for elemento in iterable if condicion}

# Tabla de cuadrados
cuadrados: dict = {x: x**2 for x in range(1, 6)}
print(f"\nCuadrados: {cuadrados}")

# Filtrar valores mayores a 50
precios: dict = {"Laptop": 999, "Mouse": 25, "Teclado": 75, "Monitor": 250}
caros: dict = {k: v for k, v in precios.items() if v > 50}
print(f"Productos caros (>50): {caros}")

# Invertir claves y valores
original: dict = {"a": 1, "b": 2, "c": 3}
invertido: dict = {v: k for k, v in original.items()}
print(f"Original: {original}")
print(f"Invertido: {invertido}")
print("\n" + "-"*60)


# ==============================================================================
# 7. DICCIONARIOS ANIDADOS
# ==============================================================================
print("\n7. DICCIONARIOS ANIDADOS")
print("="*60)

empresa: dict = {
    "nombre": "TechCorp",
    "empleados": {
        "desarrollo": ["Ana", "Luis"],
        "ventas": ["María", "Carlos"]
    },
    "ubicacion": {
        "ciudad": "Madrid",
        "pais": "España"
    }
}

print(f"\nEmpresa: {empresa}")
print(f"Nombre: {empresa['nombre']}")
print(f"Empleado de desarrollo: {empresa['empleados']['desarrollo'][0]}")
print(f"Ciudad: {empresa['ubicacion']['ciudad']}")

# Modificar valor anidado
empresa["empleados"]["desarrollo"].append("Sofía")
print(f"Tras agregar empleado: {empresa['empleados']['desarrollo']}")
print("\n" + "-"*60)


# ==============================================================================
# 8. CREACIÓN DE SETS
# ==============================================================================
print("\n8. CREACIÓN DE SETS")
print("="*60)

# Literal con llaves {}
numeros: set = {1, 2, 3, 4, 5}

# Set vacío (OJO: {} crea dict, no set)
vacio: set = set()

# Desde lista (elimina duplicados)
desde_lista: set = set([1, 2, 2, 3, 3, 4])

# Desde string
desde_string: set = set("python")

# Desde tupla
desde_tupla: set = set((1, 2, 3))

print(f"\nLiteral: {numeros}")
print(f"Desde lista (con duplicados): {desde_lista}")
print(f"Desde string: {desde_string}")
print(f"Desde tupla: {desde_tupla}")
print(f"Set vacío: {vacio} (tipo: {type(vacio)})")
print("\n" + "-"*60)


# ==============================================================================
# 9. OPERACIONES BÁSICAS CON SETS
# ==============================================================================
print("\n9. OPERACIONES BÁSICAS CON SETS")
print("="*60)

frutas: set = {"manzana", "banana", "naranja"}

print(f"\nSet original: {frutas}")

# add() agrega un elemento
frutas.add("pera")
print(f"Tras add('pera'): {frutas}")

# remove() elimina (lanza KeyError si no existe)
frutas.remove("banana")
print(f"Tras remove('banana'): {frutas}")

# discard() elimina (no lanza error si no existe)
frutas.discard("uva")
print(f"Tras discard('uva'): {frutas}")

# pop() elimina y retorna un elemento aleatorio
eliminado = frutas.pop()
print(f"Tras pop(): {frutas} (eliminado: {eliminado})")

# clear() vacía el set
frutas.clear()
print(f"Tras clear(): {frutas}")
print("\n" + "-"*60)


# ==============================================================================
# 10. OPERACIONES DE CONJUNTOS
# ==============================================================================
print("\n10. OPERACIONES DE CONJUNTOS")
print("="*60)

a: set = {1, 2, 3, 4, 5}
b: set = {4, 5, 6, 7, 8}

print(f"\nSet A: {a}")
print(f"Set B: {b}")

# Unión (|) - todos los elementos de ambos
union: set = a | b
print(f"\nUnión (a | b): {union}")

# Intersección (&) - elementos en ambos
interseccion: set = a & b
print(f"Intersección (a & b): {interseccion}")

# Diferencia (-) - elementos en A que no están en B
diferencia: set = a - b
print(f"Diferencia (a - b): {diferencia}")

# Diferencia simétrica (^) - elementos en A o B pero no en ambos
dif_simetrica: set = a ^ b
print(f"Diferencia simétrica (a ^ b): {dif_simetrica}")

# Subconjunto y superconjunto
c: set = {1, 2}
print(f"\n{c} es subconjunto de {a}: {c.issubset(a)}")
print(f"{a} es superconjunto de {c}: {a.issuperset(c)}")

# Conjuntos disjuntos (sin elementos comunes)
d: set = {10, 11, 12}
print(f"{a} y {d} son disjuntos: {a.isdisjoint(d)}")
print("\n" + "-"*60)


# ==============================================================================
# 11. SETS POR COMPRENSIÓN
# ==============================================================================
print("\n11. SETS POR COMPRENSIÓN")
print("="*60)

# Letras únicas de una frase
frase: str = "python es genial"
letras_unicas: set = {c for c in frase if c != " "}
print(f"\nFrase: '{frase}'")
print(f"Letras únicas: {letras_unicas}")

# Cuadrados únicos de una lista con duplicados
numeros: list = [1, 2, 2, 3, 3, 4]
cuadrados_unicos: set = {x**2 for x in numeros}
print(f"\nNúmeros: {numeros}")
print(f"Cuadrados únicos: {cuadrados_unicos}")
print("\n" + "-"*60)


# ==============================================================================
# 12. FROZENSET (SETS INMUTABLES)
# ==============================================================================
print("\n12. FROZENSET (SETS INMUTABLES)")
print("="*60)

# frozenset es inmutable, puede usarse como clave de dict o elemento de set
inmutable: frozenset = frozenset([1, 2, 3, 4])
print(f"\nfrozenset: {inmutable} (tipo: {type(inmutable)})")

# Puede usarse como clave de diccionario
diccionario_con_fs: dict = {inmutable: "valor"}
print(f"Dict con frozenset como clave: {diccionario_con_fs}")

# Puede ser elemento de otro set
set_de_sets: set = {frozenset([1, 2]), frozenset([3, 4])}
print(f"Set de frozensets: {set_de_sets}")

# inmutable.add(5)  # Esto lanzaría AttributeError
print("\n" + "="*60)
print("FIN DE LA GUÍA DE DICCIONARIOS Y SETS")
print("="*60)
