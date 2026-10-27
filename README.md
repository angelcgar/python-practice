# Python Practice - Fundamentos del Lenguaje

Repositorio académico dedicado al estudio sistemático de los fundamentos del lenguaje de programación Python. Este proyecto está estructurado de manera progresiva, cubriendo desde los conceptos más básicos hasta las estructuras de control esenciales, con el objetivo de proporcionar una base sólida para el desarrollo en Python.

> **Nota**: Este repositorio es un proyecto de estudio personal. Su propósito es el repaso y consolidación de los fundamentos de Python, no constituye material de distribución profesional.

## 📋 Descripción

Este repositorio constituye una guía práctica y teórica para el aprendizaje de Python desde cero. Cada módulo está organizado en carpetas temáticas que contienen:

- **Documentación teórica** (`01_teoria_y_ejemplos.py`): Explicaciones detalladas con ejemplos de código comentados y ejecutables
- **Ejercicios prácticos** (`02_ejercicios.py`): Problemas diseñados para reforzar los conceptos aprendidos
- **Soluciones completas** (`03_soluciones.py`): Implementaciones de referencia con comentarios explicativos y salidas esperadas

El enfoque pedagógico sigue una metodología de aprendizaje activo, donde la teoría se complementa con práctica inmediata y retroalimentación a través de soluciones verificadas.

## 🎯 Objetivos de Aprendizaje

- Dominar los tipos de datos fundamentales de Python y sus características
- Comprender el sistema de tipado dinámico y las anotaciones de tipo
- Aplicar correctamente todos los operadores del lenguaje
- Utilizar estructuras de control condicionales e iterativas
- Manipular cadenas de texto, listas, tuplas, diccionarios y sets
- Definir funciones con parámetros avanzados (`*args`, `**kwargs`, lambdas)
- Manejar archivos de texto, JSON y CSV
- Implementar manejo de excepciones robusto

## 📚 Contenido del Repositorio

| #   | Módulo                                           | Tema                                           | Ejercicios | Estado        |
| --- | ------------------------------------------------ | ---------------------------------------------- | ---------- | ------------- |
| 01  | [variables_y_tipos](./01_variables_y_tipos/)     | Tipos de datos, casting, anotaciones           | 10         | ✅ Completado |
| 02  | [operadores](./02_operadores/)                   | Aritméticos, lógicos, comparación, bit a bit   | 10         | ✅ Completado |
| 03  | [estructuras_control](./03_estructuras_control/) | if/else, bucles, break/continue, comprensiones | 10         | ✅ Completado |
| 04  | [cadenas](./04_cadenas/)                         | Métodos de string, slicing, formateo           | 10         | ✅ Completado |
| 05  | [listas_tuplas](./05_listas_tuplas/)             | Secuencias mutables e inmutables, matrices     | 10         | ✅ Completado |
| 06  | [diccionarios_sets](./06_diccionarios_sets/)     | Mapeos, conjuntos, operaciones de sets         | 10         | ✅ Completado |
| 07  | [funciones](./07_funciones/)                     | Parámetros, scope, lambdas, recursividad       | 10         | ✅ Completado |
| 08  | [manejo_archivos](./08_manejo_archivos/)         | Lectura/escritura, JSON, CSV, pathlib          | 10         | ✅ Completado |
| 09  | [excepciones](./09_excepciones/)                 | try/except/finally, raise, excepciones custom  | 10         | ✅ Completado |

## 🚀 Requisitos Previos

- **Python**: Versión 3.8 o superior (recomendado 3.11+)
- **Editor de código**: VS Code, PyCharm, o cualquier editor con soporte para Python
- **Conocimientos básicos**: No se requieren conocimientos previos de programación

### Verificar instalación de Python

'''bash
python --version
'''

## 💻 Uso del Repositorio

### Clonar el Repositorio

'''bash
git clone <https://github.com/tu-usuario/python-practice.git>
cd python-practice
'''

### Ejecutar los Archivos

Cada módulo contiene tres archivos. Ejecuta la teoría para ver las salidas en consola:

'''bash

# Teoría y ejemplos (muestra todas las salidas explicadas)

python 01_variables_y_tipos/01_teoria_y_ejemplos.py

# Ejercicios (completa los espacios con tu código)

python 01_variables_y_tipos/02_ejercicios.py

# Soluciones (consulta solo después de intentar resolver)

python 01_variables_y_tipos/03_soluciones.py
'''

### Nota sobre archivos generados

El módulo `08_manejo_archivos` crea una carpeta `archivos_practica/` con archivos de ejemplo. Puedes eliminarla después de estudiar sin afectar el resto del repositorio.

## 📐 Convenciones de Código

Este repositorio sigue las convenciones establecidas en PEP 8:

- **Nomenclatura**: `snake_case` para variables y funciones
- **Anotaciones de tipo**: Uso consistente de type hints (Python 3.8+)
- **Docstrings**: Documentación en funciones y módulos
- **Comentarios**: Explicaciones declarativas en español
- **Formato**: Salidas de consola con separadores visuales claros

### Ejemplo de Estilo

'''python

# Declaración con anotación de tipo

nombre_usuario: str = "Desarrollador"
edad: int = 25

# Función con type hints y docstring

def calcular_area(base: float, altura: float) -> float:
"""Calcula el área de un triángulo."""
return (base \* altura) / 2
'''

## 🎓 Metodología de Aprendizaje Recomendada

1. **Lectura teórica**: Ejecuta y estudia el archivo `01_teoria_y_ejemplos.py` del módulo
2. **Análisis de salidas**: Observa las salidas en consola y comprende cada resultado
3. **Práctica independiente**: Resuelve los ejercicios de `02_ejercicios.py` sin consultar las soluciones
4. **Verificación**: Compara tus soluciones con `03_soluciones.py`
5. **Reflexión**: Analiza las diferencias y comprende por qué la solución funciona

## 🤝 Contribuciones

Este es un repositorio de estudio personal. Sin embargo, si encuentras errores:

1. Abre un issue describiendo el problema
2. Proporciona ejemplos claros cuando sea posible

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](./LICENSE) para más detalles.

---

**Última actualización**: Octubre 2026

⭐ Si este repositorio te resulta útil para tu propio estudio, considérale una estrella.
