"""
SOLUCIONES - CADENAS DE TEXTO EN PYTHON
========================================
"""

# ==============================================================================
# EJERCICIO 1
# ==============================================================================
texto: str = "Programación en Python"

print("="*60)
print("EJERCICIO 1: Acceso y slicing")
print("="*60)
print(f"\nTexto: '{texto}'\n")

print(f"Primeros 5 caracteres: '{texto[:5]}'")
print(f"Últimos 6 caracteres: '{texto[-6:]}'")
print(f"Cada segundo carácter: '{texto[::2]}'")
print(f"Texto en reversa: '{texto[::-1]}'")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 2
# ==============================================================================
nombres: list = ["ana", "LUIS", "MaRíA", "carlos"]

print("\nEJERCICIO 2: Conversión de caso")
print("="*60)
print(f"\nLista original: {nombres}\n")

nombres_formateados: list = []
for nombre in nombres:
    nombres_formateados.append(nombre.capitalize())

print(f"Lista formateada: {nombres_formateados}")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 3
# ==============================================================================
texto: str = "Python es un lenguaje de programación. Python es poderoso."

print("\nEJERCICIO 3: Búsqueda y conteo")
print("="*60)
print(f"\nTexto: '{texto}'\n")

cantidad: int = texto.count("Python")
primera_pos: int = texto.find("Python")
ultima_pos: int = texto.rfind("Python")
termina_con: bool = texto.endswith("poderoso.")

print(f"Cantidad de 'Python': {cantidad}")
print(f"Primera aparición en posición: {primera_pos}")
print(f"Última aparición en posición: {ultima_pos}")
print(f"Termina con 'poderoso.': {termina_con}")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 4
# ==============================================================================
texto: str = "manzana,banana,naranja,uva,mango"

print("\nEJERCICIO 4: Reemplazo y división")
print("="*60)
print(f"\nTexto original: '{texto}'\n")

texto_reemplazado: str = texto.replace("banana", "pera")
print(f"Después de reemplazar: '{texto_reemplazado}'")

lista_frutas: list = texto_reemplazado.split(",")
print(f"Lista dividida: {lista_frutas}")

primeros_tres: list = lista_frutas[:3]
resultado: str = " y ".join(primeros_tres)
print(f"Primeros 3 unidos: '{resultado}'")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 5
# ==============================================================================
textos: list = ["123", "Python", "45.67", "   ", "ABC123"]

print("\nEJERCICIO 5: Verificación de tipo")
print("="*60)

for texto in textos:
    print(f"\nTexto: '{texto}'")
    print(f"  isdigit(): {texto.isdigit()}")
    print(f"  isalpha(): {texto.isalpha()}")
    print(f"  isalnum(): {texto.isalnum()}")

print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 6
# ==============================================================================
texto: str = "   Python es genial   "

print("\nEJERCICIO 6: Eliminación de espacios")
print("="*60)
print(f"\nTexto original: '{texto}' (longitud: {len(texto)})\n")

sin_espacios_ambos: str = texto.strip()
sin_espacios_inicio: str = texto.lstrip()
sin_espacios_final: str = texto.rstrip()
sin_espacios_total: str = texto.replace(" ", "")

print(f"strip(): '{sin_espacios_ambos}' (longitud: {len(sin_espacios_ambos)})")
print(f"lstrip(): '{sin_espacios_inicio}' (longitud: {len(sin_espacios_inicio)})")
print(f"rstrip(): '{sin_espacios_final}' (longitud: {len(sin_espacios_final)})")
print(f"replace(' ', ''): '{sin_espacios_total}' (longitud: {len(sin_espacios_total)})")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 7
# ==============================================================================
productos: list = ["Laptop", "Mouse", "Teclado", "Monitor"]

print("\nEJERCICIO 7: Alineación")
print("="*60)
print()

for producto in productos:
    print(producto.rjust(15, "."))

print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 8
# ==============================================================================
precio: float = 1234567.89

print("\nEJERCICIO 8: Formateo de números")
print("="*60)
print(f"\nPrecio original: {precio}\n")

print(f"Con 2 decimales: {precio:.2f}")
print(f"Con separador de miles: {precio:,.2f}")
print(f"Con símbolo de moneda: ${precio:,.2f}")
print(f"Notación científica: {precio:.3e}")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 9
# ==============================================================================
parrafo: str = """Python es un lenguaje de programación versátil.
Es conocido por su sintaxis clara y legible.
Python se usa en web, ciencia de datos, automatización y más."""

print("\nEJERCICIO 9: Análisis de texto")
print("="*60)
print(f"\nPárrafo:\n{parrafo}\n")

# Caracteres sin espacios
sin_espacios: str = parrafo.replace(" ", "").replace("\n", "")
caracteres: int = len(sin_espacios)

# Palabras
palabras: list = parrafo.split()
num_palabras: int = len(palabras)

# Oraciones
oraciones: int = parrafo.count(".")

# Palabra más larga
palabra_mas_larga: str = max(palabras, key=len)

print(f"Caracteres (sin espacios): {caracteres}")
print(f"Número de palabras: {num_palabras}")
print(f"Número de oraciones: {oraciones}")
print(f"Palabra más larga: '{palabra_mas_larga}' ({len(palabra_mas_larga)} caracteres)")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 10
# ==============================================================================
texto: str = "hOLA mUNDO dE pYTHON"

print("\nEJERCICIO 10: Transformación compleja")
print("="*60)
print(f"\nTexto original: '{texto}'\n")

# Paso 1: minúsculas
paso1: str = texto.lower()
print(f"1. Minúsculas: '{paso1}'")

# Paso 2: reemplazo
paso2: str = paso1.replace("mundo", "universo")
print(f"2. Reemplazo: '{paso2}'")

# Paso 3: capitalizar
paso3: str = paso2.capitalize()
print(f"3. Capitalizar: '{paso3}'")

# Paso 4: centrar
paso4: str = paso3.center(40, "*")
print(f"4. Centrar: '{paso4}'")
print("\n" + "="*60)
