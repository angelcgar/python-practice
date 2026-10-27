"""
EJERCICIOS - FUNCIONES EN PYTHON
=================================
Resuelve cada ejercicio. No mires las soluciones hasta terminar.
"""

# ==============================================================================
# EJERCICIO 1: Función básica con retorno
# ==============================================================================
# Crea una función llamada 'calcular_area_circulo' que reciba el radio (float)
# y retorne el área (float). Usa math.pi.
# Imprime el resultado para un radio de 5.0.

# Tu código aquí:



# ==============================================================================
# EJERCICIO 2: Parámetros por defecto
# ==============================================================================
# Crea una función 'generar_reporte' que reciba 'titulo' (str) y 'tipo' (str).
# El parámetro 'tipo' debe tener por defecto el valor "PDF".
# La función debe retornar un string: "Generando [titulo] en formato [tipo]".
# Llámala dos veces: una sin especificar tipo, y otra con tipo "CSV".

# Tu código aquí:



# ==============================================================================
# EJERCICIO 3: *args
# ==============================================================================
# Crea una función 'multiplicar_todos' que reciba una cantidad variable de números
# (*args: int | float) y retorne su producto total.
# Si no se pasa ningún número, debe retornar 1.
# Prueba con (2, 3, 4) y con (5, 10).

# Tu código aquí:



# ==============================================================================
# EJERCICIO 4: **kwargs
# ==============================================================================
# Crea una función 'crear_html_tag' que reciba el nombre del tag como primer
# argumento posicional (str) y atributos variables (**kwargs: str).
# Debe retornar un string con el tag HTML formado.
# Ejemplo: crear_html_tag("a", href="url", class="link") -> '<a href="url" class="link">'
# (Nota: solo abre el tag, no te preocupes por cerrarlo).

# Tu código aquí:



# ==============================================================================
# EJERCICIO 5: Retorno múltiple y desempaquetado
# ==============================================================================
# Crea una función 'analizar_texto' que reciba un string y retorne 3 valores:
# 1. Cantidad de caracteres totales.
# 2. Cantidad de palabras.
# 3. El texto en mayúsculas.
# Llama a la función con el texto "Python es genial" y desempaqueta los 3 resultados
# en variables separadas para imprimirlos.

# Tu código aquí:



# ==============================================================================
# EJERCICIO 6: Scope (Alcance)
# ==============================================================================
# Declara una variable global 'contador' con valor 0.
# Crea una función 'incrementar' que modifique la variable global sumándole 1.
# Llama a la función 3 veces e imprime el valor final de 'contador'.
# (Pista: usa la palabra reservada 'global').

# Tu código aquí:



# ==============================================================================
# EJERCICIO 7: Funciones Lambda
# ==============================================================================
# Tienes una lista de diccionarios representando productos:
# productos = [{"nombre": "Laptop", "precio": 1000}, {"nombre": "Mouse", "precio": 50}, {"nombre": "Teclado", "precio": 150}]
# Usa la función sorted() y una función lambda para ordenar la lista
# de productos de mayor a menor precio. Imprime la lista ordenada.

productos: list[dict[str, str | int]] = [
    {"nombre": "Laptop", "precio": 1000}, 
    {"nombre": "Mouse", "precio": 50}, 
    {"nombre": "Teclado", "precio": 150}
]

# Tu código aquí:



# ==============================================================================
# EJERCICIO 8: Funciones como argumentos
# ==============================================================================
# Crea una función 'aplicar_a_lista' que reciba una lista de números y una función.
# Debe retornar una nueva lista donde la función recibida se haya aplicado a cada elemento.
# Crea dos funciones auxiliares: 'al_cuadrado' y 'es_par' (que retorne True/False).
# Prueba 'aplicar_a_lista' con ambas funciones sobre la lista [1, 2, 3, 4, 5].

# Tu código aquí:



# ==============================================================================
# EJERCICIO 9: Recursividad
# ==============================================================================
# Crea una función recursiva 'suma_digitos' que reciba un número entero positivo
# y retorne la suma de sus dígitos.
# Ejemplo: 142 -> 1 + 4 + 2 = 7.
# Imprime el resultado para 9876.

# Tu código aquí:



# ==============================================================================
# EJERCICIO 10: Docstring y Type Hinting profesional
# ==============================================================================
# Crea una función llamada 'filtrar_adultos' que reciba una lista de diccionarios
# (donde cada diccionario tiene 'nombre' y 'edad').
# Debe retornar una lista con los nombres de las personas de 18 años o más.
# Asegúrate de incluir Type Hinting completo y un Docstring profesional (estilo Google o Sphinx).

# Tu código aquí:
