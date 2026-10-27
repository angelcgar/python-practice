"""
OPERADORES EN PYTHON - GUÍA COMPLETA
=====================================
Todos los operadores disponibles, explicados, con anotaciones de tipo.
"""

# ==============================================================================
# 1. OPERADORES ARITMÉTICOS
# ==============================================================================
# Operan sobre números y retornan números.

a: int = 17
b: int = 5

suma: int = a + b            # Suma
resta: int = a - b           # Resta
multiplicacion: int = a * b  # Multiplicación
division: float = a / b      # División (siempre retorna float)
division_entera: int = a // b  # División entera (trunca hacia abajo)
modulo: int = a % b          # Resto de la división
potencia: int = a ** b       # Potencia

print("--- Aritméticos ---")
print(f"17 + 5 = {suma}")
print(f"17 - 5 = {resta}")
print(f"17 * 5 = {multiplicacion}")
print(f"17 / 5 = {division}")
print(f"17 // 5 = {division_entera}")
print(f"17 % 5 = {modulo}")
print(f"17 ** 5 = {potencia}")
# Salida:
# 17 + 5 = 22
# 17 - 5 = 12
# 17 * 5 = 85
# 17 / 5 = 3.4
# 17 // 5 = 3
# 17 % 5 = 2
# 17 ** 5 = 1419857


# ==============================================================================
# 2. OPERADORES DE COMPARACIÓN
# ==============================================================================
# Comparan dos valores y retornan bool (True o False).

x: int = 10
y: int = 20

igual: bool = x == y         # ¿Iguales?
diferente: bool = x != y     # ¿Diferentes?
mayor: bool = x > y          # ¿Mayor que?
menor: bool = x < y          # ¿Menor que?
mayor_igual: bool = x >= y   # ¿Mayor o igual?
menor_igual: bool = x <= y   # ¿Menor o igual?

print("\n--- Comparación ---")
print(f"10 == 20: {igual}")
print(f"10 != 20: {diferente}")
print(f"10 > 20: {mayor}")
print(f"10 < 20: {menor}")
print(f"10 >= 20: {mayor_igual}")
print(f"10 <= 20: {menor_igual}")
# Salida: False, True, False, True, False, True


# ==============================================================================
# 3. OPERADORES LÓGICOS
# ==============================================================================
# Combinan expresiones booleanas. Usan evaluación de corto circuito.

p: bool = True
q: bool = False

y_logico: bool = p and q     # True si ambos son True
o_logico: bool = p or q      # True si al menos uno es True
negacion: bool = not p       # Invierte el valor

print("\n--- Lógicos ---")
print(f"True and False: {y_logico}")
print(f"True or False: {o_logico}")
print(f"not True: {negacion}")
# Salida: False, True, False

# Corto circuito: Python evalúa solo lo necesario
resultado_1: bool = False and print("Esto no se imprime")  # No ejecuta print
resultado_2: bool = True or print("Esto tampoco")          # No ejecuta print


# ==============================================================================
# 4. OPERADORES DE ASIGNACIÓN
# ==============================================================================
# Asignan valores a variables. Los compuestos modifican y asignan en un paso.

contador: int = 10         # Asignación básica

contador += 5              # contador = contador + 5 → 15
contador -= 3              # contador = contador - 3 → 12
contador *= 2              # contador = contador * 2 → 24
contador /= 4              # contador = contador / 4 → 6.0 (float)
contador //= 2             # contador = contador // 2 → 3.0
contador %= 2              # contador = contador % 2 → 1.0
contador **= 3             # contador = contador ** 3 → 1.0

print("\n--- Asignación ---")
print(f"Resultado final: {contador}, tipo: {type(contador)}")
# Salida: 1.0, tipo: <class 'float'>


# ==============================================================================
# 5. OPERADORES DE IDENTIDAD
# ==============================================================================
# Comparan si dos variables apuntan al MISMO objeto en memoria (no solo valor).

lista_a: list = [1, 2, 3]
lista_b: list = [1, 2, 3]
lista_c: list = lista_a

es_mismo_objeto: bool = lista_a is lista_c      # True (mismo objeto)
no_es_mismo: bool = lista_a is not lista_b      # True (objetos distintos)
igualdad_valor: bool = lista_a == lista_b       # True (mismo valor, distinto objeto)

print("\n--- Identidad ---")
print(f"lista_a is lista_c: {es_mismo_objeto}")
print(f"lista_a is not lista_b: {no_es_mismo}")
print(f"lista_a == lista_b: {igualdad_valor}")
print(f"id(lista_a): {id(lista_a)}, id(lista_c): {id(lista_c)}")
# Salida: True, True, True, ids iguales


# ==============================================================================
# 6. OPERADORES DE PERTENENCIA
# ==============================================================================
# Verifican si un valor existe dentro de una secuencia (str, list, tuple, dict, set).

texto: str = "Python"
numeros: list = [1, 2, 3, 4, 5]
persona: dict = {"nombre": "Ana", "edad": 30}

esta_en_texto: bool = "Py" in texto           # True
no_esta: bool = "Java" not in texto           # True
esta_en_lista: bool = 3 in numeros            # True
es_clave: bool = "nombre" in persona          # True (busca en claves)
no_es_clave: bool = "Ana" not in persona      # True (no busca en valores)

print("\n--- Pertenencia ---")
print(f"'Py' in 'Python': {esta_en_texto}")
print(f"'Java' not in 'Python': {no_esta}")
print(f"3 in [1,2,3,4,5]: {esta_en_lista}")
print(f"'nombre' in persona: {es_clave}")
print(f"'Ana' not in persona: {no_es_clave}")
# Salida: True, True, True, True, True


# ==============================================================================
# 7. OPERADORES BIT A BIT
# ==============================================================================
# Operan sobre los bits de números enteros.

m: int = 12   # Binario: 1100
n: int = 10   # Binario: 1010

and_bit: int = m & n     # AND bit a bit: 1000 = 8
or_bit: int = m | n      # OR bit a bit: 1110 = 14
xor_bit: int = m ^ n     # XOR bit a bit: 0110 = 6
not_bit: int = ~m        # NOT bit a bit: -(m+1) = -13
shift_izq: int = m << 2  # Desplaza 2 bits a la izquierda: 110000 = 48
shift_der: int = m >> 2  # Desplaza 2 bits a la derecha: 11 = 3

print("\n--- Bit a Bit ---")
print(f"12 & 10 = {and_bit} (binario: {bin(and_bit)})")
print(f"12 | 10 = {or_bit} (binario: {bin(or_bit)})")
print(f"12 ^ 10 = {xor_bit} (binario: {bin(xor_bit)})")
print(f"~12 = {not_bit}")
print(f"12 << 2 = {shift_izq} (binario: {bin(shift_izq)})")
print(f"12 >> 2 = {shift_der} (binario: {bin(shift_der)})")
# Salida: 8, 14, 6, -13, 48, 3


# ==============================================================================
# 8. OPERADOR WALRUS (:=) - Python 3.8+
# ==============================================================================
# Asigna y retorna un valor en la misma expresión. Útil en condicionales y while.

# Sin walrus: calculas y luego usas
datos: list = [1, 5, 8, 12, 3, 20]
total: int = sum(datos)
if total > 30:
    print(f"Total alto: {total}")

# Con walrus: asigna y usa en una línea
if (total_walrus := sum(datos)) > 30:
    print(f"Total alto con walrus: {total_walrus}")

print("\n--- Walrus ---")
print(f"total_walrus: {total_walrus}")
# Salida: Total alto: 49, Total alto con walrus: 49, total_walrus: 49


# ==============================================================================
# 9. OPERADORES EN CADENAS
# ==============================================================================
# Algunos operadores funcionan también con strings.

nombre: str = "Hola"
apellido: str = "Mundo"

concatenacion: str = nombre + " " + apellido  # Concatenación
repeticion: str = nombre * 3                  # Repetición

print("\n--- Operadores en strings ---")
print(f"Concatenación: {concatenacion}")
print(f"Repetición: {repeticion}")
# Salida: Hola Mundo, HolaHolaHola


# ==============================================================================
# 10. PRECEDENCIA DE OPERADORES
# ==============================================================================
# Orden de evaluación (de mayor a menor prioridad):
# 1. ()        Paréntesis
# 2. **        Potencia
# 3. ~ + -     Not bit a bit, positivo, negativo unario
# 4. * / // %  Multiplicación, división, módulo
# 5. + -       Suma, resta
# 6. << >>     Desplazamientos bit a bit
# 7. &         AND bit a bit
# 8. ^         XOR bit a bit
# 9. |         OR bit a bit
# 10. == != < > <= >= is in  Comparaciones e identidad
# 11. not      NOT lógico
# 12. and      AND lógico
# 13. or       OR lógico

resultado: int = 2 + 3 * 4 ** 2  # 2 + 3 * 16 = 2 + 48 = 50
resultado_parentesis: int = (2 + 3) * 4 ** 2  # 5 * 16 = 80

print("\n--- Precedencia ---")
print(f"2 + 3 * 4 ** 2 = {resultado}")
print(f"(2 + 3) * 4 ** 2 = {resultado_parentesis}")
# Salida: 50, 80
