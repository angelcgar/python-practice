"""
CADENAS DE TEXTO EN PYTHON - GUÍA COMPLETA
===========================================
Todos los métodos y operaciones con strings, con salidas formateadas.
"""

# ==============================================================================
# 1. CREACIÓN Y ACCESO A CARACTERES
# ==============================================================================
print("="*60)
print("1. CREACIÓN Y ACCESO A CARACTERES")
print("="*60)

texto: str = "Python"

print(f"\nTexto original: '{texto}'")
print(f"Primer carácter: '{texto[0]}'")
print(f"Último carácter: '{texto[-1]}'")
print(f"Carácter en posición 2: '{texto[2]}'")

print("\n" + "-"*60)


# ==============================================================================
# 2. SLICING (SEGMENTACIÓN)
# ==============================================================================
print("\n2. SLICING (SEGMENTACIÓN)")
print("="*60)

texto: str = "Python"

print(f"\nTexto: '{texto}'")
print(f"texto[0:3] (posiciones 0,1,2): '{texto[0:3]}'")
print(f"texto[:3] (desde inicio hasta 3): '{texto[:3]}'")
print(f"texto[3:] (desde 3 hasta final): '{texto[3:]}'")
print(f"texto[::2] (cada 2 caracteres): '{texto[::2]}'")
print(f"texto[::-1] (inverso): '{texto[::-1]}'")

print("\n" + "-"*60)


# ==============================================================================
# 3. MÉTODOS DE CONVERSIÓN DE CASO
# ==============================================================================
print("\n3. MÉTODOS DE CONVERSIÓN DE CASO")
print("="*60)

texto: str = "Hola Mundo Python"

print(f"\nTexto original: '{texto}'")
print(f"texto.upper(): '{texto.upper()}'")
print(f"texto.lower(): '{texto.lower()}'")
print(f"texto.capitalize(): '{texto.capitalize()}'")
print(f"texto.title(): '{texto.title()}'")
print(f"texto.swapcase(): '{texto.swapcase()}'")

print("\n" + "-"*60)


# ==============================================================================
# 4. MÉTODOS DE BÚSQUEDA Y CONTEO
# ==============================================================================
print("\n4. MÉTODOS DE BÚSQUEDA Y CONTEO")
print("="*60)

texto: str = "Python es genial y Python es poderoso"

print(f"\nTexto: '{texto}'")
print(f"texto.find('Python'): {texto.find('Python')}")
print(f"texto.find('Java'): {texto.find('Java')}")
print(f"texto.rfind('Python'): {texto.rfind('Python')}")
print(f"texto.count('Python'): {texto.count('Python')}")
print(f"texto.count('es'): {texto.count('es')}")
print(f"'Python' in texto: {'Python' in texto}")
print(f"texto.startswith('Python'): {texto.startswith('Python')}")
print(f"texto.endswith('poderoso'): {texto.endswith('poderoso')}")

print("\n" + "-"*60)


# ==============================================================================
# 5. MÉTODOS DE REEMPLAZO Y DIVISIÓN
# ==============================================================================
print("\n5. MÉTODOS DE REEMPLAZO Y DIVISIÓN")
print("="*60)

texto: str = "Python es bueno, Python es rápido"

print(f"\nTexto original: '{texto}'")
print(f"texto.replace('Python', 'JavaScript'): '{texto.replace('Python', 'JavaScript')}'")
print(f"texto.replace('Python', 'JS', 1): '{texto.replace('Python', 'JS', 1)}'")

texto_dividir: str = "manzana,banana,naranja,uva"
print(f"\nTexto a dividir: '{texto_dividir}'")
print(f"texto.split(','): {texto_dividir.split(',')}")
print(f"texto.split(',', 2): {texto_dividir.split(',', 2)}")

texto_unir: list = ["Python", "es", "genial"]
print(f"\nLista a unir: {texto_unir}")
print(f"' '.join(lista): '{' '.join(texto_unir)}'")
print(f"'-'.join(lista): '{'-'.join(texto_unir)}'")

print("\n" + "-"*60)


# ==============================================================================
# 6. MÉTODOS DE VERIFICACIÓN
# ==============================================================================
print("\n6. MÉTODOS DE VERIFICACIÓN")
print("="*60)

textos: list = ["Python3", "12345", "Python", "   ", "PYTHON", "python"]

print(f"\nVerificaciones:")
for t in textos:
    print(f"\n  Texto: '{t}'")
    print(f"    isalnum(): {t.isalnum()}")
    print(f"    isalpha(): {t.isalpha()}")
    print(f"    isdigit(): {t.isdigit()}")
    print(f"    islower(): {t.islower()}")
    print(f"    isupper(): {t.isupper()}")
    print(f"    isspace(): {t.isspace()}")

print("\n" + "-"*60)


# ==============================================================================
# 7. MÉTODOS DE ELIMINACIÓN DE ESPACIOS
# ==============================================================================
print("\n7. MÉTODOS DE ELIMINACIÓN DE ESPACIOS")
print("="*60)

texto: str = "   Python   "

print(f"\nTexto original: '{texto}'")
print(f"len(texto): {len(texto)}")
print(f"texto.strip(): '{texto.strip()}'")
print(f"texto.lstrip(): '{texto.lstrip()}'")
print(f"texto.rstrip(): '{texto.rstrip()}'")

texto_con_guiones: str = "---Python---"
print(f"\nTexto con guiones: '{texto_con_guiones}'")
print(f"texto.strip('-'): '{texto_con_guiones.strip('-')}'")

print("\n" + "-"*60)


# ==============================================================================
# 8. MÉTODOS DE ALINEACIÓN Y RELLENO
# ==============================================================================
print("\n8. MÉTODOS DE ALINEACIÓN Y RELLENO")
print("="*60)

texto: str = "Python"

print(f"\nTexto: '{texto}'")
print(f"texto.center(20): '{texto.center(20)}'")
print(f"texto.center(20, '*'): '{texto.center(20, '*')}'")
print(f"texto.ljust(20): '{texto.ljust(20)}'")
print(f"texto.ljust(20, '-'): '{texto.ljust(20, '-')}'")
print(f"texto.rjust(20): '{texto.rjust(20)}'")
print(f"texto.rjust(20, '.'): '{texto.rjust(20, '.')}'")
print(f"texto.zfill(10): '{texto.zfill(10)}'")

print("\n" + "-"*60)


# ==============================================================================
# 9. FORMATEO DE CADENAS
# ==============================================================================
print("\n9. FORMATEO DE CADENAS")
print("="*60)

nombre: str = "Ana"
edad: int = 30
altura: float = 1.75
precio: float = 99.99

# f-strings (Python 3.6+)
print(f"\n--- f-strings ---")
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"Altura: {altura:.2f} metros")
print(f"En 5 años tendrá {edad + 5} años")

# format()
print(f"\n--- format() ---")
print("Nombre: {}".format(nombre))
print("Edad: {} años".format(edad))
print("Nombre: {0}, Edad: {1}".format(nombre, edad))
print("Nombre: {nombre}, Edad: {edad}".format(nombre=nombre, edad=edad))

# Formato de números
print(f"\n--- Formato de números ---")
print(f"Entero con ceros: {42:05d}")
print(f"Flotante 2 decimales: {3.14159:.2f}")
print(f"Porcentaje: {0.856:.1%}")
print(f"Separador de miles: {1000000:,}")
print(f"Notación científica: {1234567:.2e}")

print("\n" + "-"*60)


# ==============================================================================
# 10. CARACTERES ESPECIALES Y ESCAPES
# ==============================================================================
print("\n10. CARACTERES ESPECIALES Y ESCAPES")
print("="*60)

print(f"\nSalto de línea:\nLínea 1\nLínea 2")
print(f"Tabulación:\tColumna 1\tColumna 2")
print(f"Comilla simple: 'texto'")
print(f"Comilla doble: \"texto\"")
print(f"Backslash: \\")

# Raw strings (no procesan escapes)
ruta: str = r"C:\nueva\carpeta"
print(f"\nRaw string: '{ruta}'")

# Strings multilínea
multilinea: str = """
Este es un texto
que abarca
múltiples líneas
"""
print(f"\nMultilínea:{multilinea}")

print("\n" + "-"*60)


# ==============================================================================
# 11. OPERACIONES CON CADENAS
# ==============================================================================
print("\n11. OPERACIONES CON CADENAS")
print("="*60)

texto1: str = "Hola"
texto2: str = "Mundo"

print(f"\nConcatenación: '{texto1 + ' ' + texto2}'")
print(f"Repetición: '{texto1 * 3}'")
print(f"Longitud de '{texto1}': {len(texto1)}")

# Comparación
print(f"\nComparación:")
print(f"'abc' < 'def': {'abc' < 'def'}")
print(f"'Python' == 'python': {'Python' == 'python'}")

print("\n" + "-"*60)


# ==============================================================================
# 12. MÉTODOS AVANZADOS
# ==============================================================================
print("\n12. MÉTODOS AVANZADOS")
print("="*60)

# partition y rpartition
texto: str = "usuario@dominio.com"
print(f"\nTexto: '{texto}'")
print(f"texto.partition('@'): {texto.partition('@')}")
print(f"texto.rpartition('@'): {texto.rpartition('@')}")

# splitlines
texto_multilinea: str = "línea1\nlínea2\nlínea3"
print(f"\nTexto multilínea:\n{texto_multilinea}")
print(f"splitlines(): {texto_multilinea.splitlines()}")

# expandtabs
texto_tabs: str = "col1\tcol2\tcol3"
print(f"\nTexto con tabs: '{texto_tabs}'")
print(f"expandtabs(4):\n'{texto_tabs.expandtabs(4)}'")

# translate y maketrans
texto: str = "hola mundo"
tabla: dict = str.maketrans("aeiou", "12345")
print(f"\nTexto: '{texto}'")
print(f"translate(vocales a números): '{texto.translate(tabla)}'")

print("\n" + "="*60)
print("FIN DE LA GUÍA DE CADENAS")
print("="*60)
