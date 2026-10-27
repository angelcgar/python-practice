"""
EJERCICIOS - EXCEPCIONES EN PYTHON
===================================
Resuelve cada ejercicio. No mires las soluciones hasta terminar.
"""

# ==============================================================================
# EJERCICIO 1: try/except básico
# ==============================================================================
# Crea una función 'dividir' que reciba dos números (a y b).
# Debe retornar el resultado de a / b.
# Si b es cero, debe capturar ZeroDivisionError e imprimir un mensaje claro.
# Prueba con: dividir(10, 2), dividir(10, 0)

# Tu código aquí:



# ==============================================================================
# EJERCICIO 2: ValueError en conversión
# ==============================================================================
# Crea una función 'convertir_a_entero' que reciba un string.
# Intenta convertirlo a int. Si falla, captura ValueError e imprime
# un mensaje indicando que el string no es un número válido.
# Prueba con: "42", "hola", "3.14"

# Tu código aquí:



# ==============================================================================
# EJERCICIO 3: Múltiples excepciones
# ==============================================================================
# Crea una función 'acceder_a_lista' que reciba una lista y un índice.
# Debe capturar IndexError si el índice no existe, y TypeError si el
# índice no es un entero. Imprime un mensaje diferente para cada caso.
# Prueba con: lista=[1,2,3], índices: 1, 10, "a"

# Tu código aquí:



# ==============================================================================
# EJERCICIO 4: Cláusula `as`
# ==============================================================================
# Intenta abrir un archivo llamado 'no_existe.txt' en modo lectura.
# Captura FileNotFoundError usando 'as e' e imprime:
# - El tipo de excepción (type(e).__name__)
# - El mensaje del error (e)
# - Los argumentos del error (e.args)

# Tu código aquí:



# ==============================================================================
# EJERCICIO 5: try/except/else
# ==============================================================================
# Crea una función 'procesar_numero' que reciba un string.
# En try: intenta convertirlo a float.
# En except ValueError: imprime que no es un número válido.
# En else: imprime el número convertido y su cuadrado.
# Prueba con: "25", "abc", "7.5"

# Tu código aquí:



# ==============================================================================
# EJERCICIO 6: try/except/finally
# ==============================================================================
# Crea una función 'leer_archivo_seguro' que reciba una ruta de archivo.
# En try: intenta abrir y leer el archivo.
# En except FileNotFoundError: imprime que el archivo no existe.
# En finally: imprime "Operación de lectura finalizada" (siempre se ejecuta).
# Prueba con un archivo existente y uno inexistente.

# Tu código aquí:



# ==============================================================================
# EJERCICIO 7: Validación de entrada
# ==============================================================================
# Crea una función 'pedir_edad' que reciba un string simulando entrada del usuario.
# Debe validar que:
# - Sea un número entero (ValueError si no lo es)
# - Esté entre 0 y 120 (ValueError personalizado si está fuera de rango)
# Si es válido, retorna la edad como int.
# Prueba con: "25", "abc", "150", "-5"

# Tu código aquí:



# ==============================================================================
# EJERCICIO 8: KeyError en diccionarios
# ==============================================================================
# Tienes el diccionario: usuario = {"nombre": "Ana", "edad": 30}
# Crea una función 'obtener_valor' que reciba el diccionario y una clave.
# Debe retornar el valor si existe, o capturar KeyError e imprimir
# "La clave 'X' no existe" retornando None.
# Prueba con claves: "nombre", "telefono", "edad"

usuario: dict = {"nombre": "Ana", "edad": 30}

# Tu código aquí:



# ==============================================================================
# EJERCICIO 9: Excepción personalizada
# ==============================================================================
# Crea una excepción personalizada 'TemperaturaInvalidaError' que herede de Exception.
# Debe recibir la temperatura y un mensaje.
# Crea una función 'verificar_temperatura' que reciba un float.
# Si la temperatura es menor a -273.15 (cero absoluto), lanza la excepción.
# Prueba con: 25.0, -300.0

# Tu código aquí:



# ==============================================================================
# EJERCICIO 10: Combinación completa
# ==============================================================================
# Crea una función 'procesar_lista_numeros' que reciba una lista de strings.
# Para cada string:
# - Intenta convertirlo a int.
# - Si es válido, imprime el número.
# - Si no es válido, imprime un warning y continúa (no detener el proceso).
# Al final, imprime cuántos números válidos e inválidos se procesaron.
# Usa try/except dentro del bucle.
# Prueba con: ["10", "abc", "20", "xyz", "30"]

# Tu código aquí:
