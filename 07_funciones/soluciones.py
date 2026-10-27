"""
SOLUCIONES - FUNCIONES EN PYTHON
=================================
"""
import math

# ==============================================================================
# EJERCICIO 1
# ==============================================================================
def calcular_area_circulo(radio: float) -> float:
    return math.pi * (radio ** 2)

print("="*60)
print("EJERCICIO 1: Función básica con retorno")
print("="*60)
print(f"\nÁrea de círculo con radio 5.0: {calcular_area_circulo(5.0):.2f}")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 2
# ==============================================================================
def generar_reporte(titulo: str, tipo: str = "PDF") -> str:
    return f"Generando {titulo} en formato {tipo}"

print("\nEJERCICIO 2: Parámetros por defecto")
print("="*60)
print(f"\n{generar_reporte('Ventas Anuales')}")
print(f"{generar_reporte('Inventario', 'CSV')}")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 3
# ==============================================================================
def multiplicar_todos(*numeros: int | float) -> int | float:
    if not numeros:
        return 1
    resultado = 1
    for n in numeros:
        resultado *= n
    return resultado

print("\nEJERCICIO 3: *args")
print("="*60)
print(f"\nmultiplicar_todos(2, 3, 4): {multiplicar_todos(2, 3, 4)}")
print(f"multiplicar_todos(5, 10): {multiplicar_todos(5, 10)}")
print(f"multiplicar_todos(): {multiplicar_todos()}")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 4
# ==============================================================================
def crear_html_tag(tag: str, **atributos: str) -> str:
    attrs_str = " ".join([f'{k}="{v}"' for k, v in atributos.items()])
    if attrs_str:
        return f"<{tag} {attrs_str}>"
    return f"<{tag}>"

print("\nEJERCICIO 4: **kwargs")
print("="*60)
print(f"\n{crear_html_tag('a', href='https://python.org', class_='link')}")
print(f"{crear_html_tag('img', src='foto.jpg', alt='Mi foto')}")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 5
# ==============================================================================
def analizar_texto(texto: str) -> tuple[int, int, str]:
    caracteres = len(texto)
    palabras = len(texto.split())
    mayusculas = texto.upper()
    return caracteres, palabras, mayusculas

print("\nEJERCICIO 5: Retorno múltiple y desempaquetado")
print("="*60)
texto_analisis = "Python es genial"
chars, words, upper_text = analizar_texto(texto_analisis)
print(f"\nTexto: '{texto_analisis}'")
print(f"Caracteres: {chars}")
print(f"Palabras: {words}")
print(f"Mayúsculas: '{upper_text}'")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 6
# ==============================================================================
contador: int = 0

def incrementar() -> None:
    global contador
    contador += 1

print("\nEJERCICIO 6: Scope (Alcance)")
print("="*60)
incrementar()
incrementar()
incrementar()
print(f"\nValor final de contador global: {contador}")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 7
# ==============================================================================
productos: list[dict[str, str | int]] = [
    {"nombre": "Laptop", "precio": 1000}, 
    {"nombre": "Mouse", "precio": 50}, 
    {"nombre": "Teclado", "precio": 150}
]

print("\nEJERCICIO 7: Funciones Lambda")
print("="*60)
productos_ordenados = sorted(productos, key=lambda p: p["precio"], reverse=True)
print(f"\nProductos ordenados por precio (mayor a menor):")
for p in productos_ordenados:
    print(f"  {p['nombre']}: ${p['precio']}")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 8
# ==============================================================================
def aplicar_a_lista(lista: list[int], funcion) -> list:
    return [funcion(x) for x in lista]

def al_cuadrado(x: int) -> int:
    return x ** 2

def es_par(x: int) -> bool:
    return x % 2 == 0

print("\nEJERCICIO 8: Funciones como argumentos")
print("="*60)
numeros = [1, 2, 3, 4, 5]
print(f"\nLista original: {numeros}")
print(f"Al cuadrado: {aplicar_a_lista(numeros, al_cuadrado)}")
print(f"Es par (booleanos): {aplicar_a_lista(numeros, es_par)}")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 9
# ==============================================================================
def suma_digitos(n: int) -> int:
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

print("\nEJERCICIO 9: Recursividad")
print("="*60)
print(f"\nSuma de dígitos de 9876: {suma_digitos(9876)}")
print(f"Suma de dígitos de 142: {suma_digitos(142)}")
print("\n" + "-"*60)


# ==============================================================================
# EJERCICIO 10
# ==============================================================================
def filtrar_adultos(usuarios: list[dict[str, str | int]]) -> list[str]:
    """
    Filtra una lista de usuarios y retorna los nombres de los mayores de edad.
    
    Args:
        usuarios (list[dict[str, str | int]]): Lista de diccionarios que deben 
                                               contener las claves 'nombre' (str) 
                                               y 'edad' (int).
                                               
    Returns:
        list[str]: Lista con los nombres de los usuarios que tienen 18 años o más.
    """
    return [u["nombre"] for u in usuarios if u.get("edad", 0) >= 18]

print("\nEJERCICIO 10: Docstring y Type Hinting profesional")
print("="*60)
data_usuarios = [
    {"nombre": "Ana", "edad": 22},
    {"nombre": "Luis", "edad": 16},
    {"nombre": "María", "edad": 18}
]
print(f"\nUsuarios adultos: {filtrar_adultos(data_usuarios)}")
print("\n" + "="*60)
