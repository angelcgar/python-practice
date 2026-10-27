# Python Practice - Fundamentos del Lenguaje

Repositorio académico dedicado al estudio sistemático de los fundamentos del lenguaje de programación Python. Este proyecto está estructurado de manera progresiva, cubriendo desde los conceptos más básicos hasta las estructuras de control esenciales, con el objetivo de proporcionar una base sólida para el desarrollo en Python.

## 📋 Descripción

Este repositorio constituye una guía práctica y teórica para el aprendizaje de Python desde cero. Cada módulo está organizado en carpetas temáticas que contienen:

- **Documentación teórica**: Explicaciones detalladas con ejemplos de código comentados
- **Ejercicios prácticos**: Problemas diseñados para reforzar los conceptos aprendidos
- **Soluciones completas**: Implementaciones de referencia con comentarios explicativos

El enfoque pedagógico sigue una metodología de aprendizaje activo, donde la teoría se complementa con práctica inmediata y retroalimentación a través de soluciones verificadas.

## 🎯 Objetivos de Aprendizaje

- Dominar los tipos de datos fundamentales de Python y sus características
- Comprender el sistema de tipado dinámico y las anotaciones de tipo
- Aplicar correctamente todos los operadores del lenguaje
- Desarrollar habilidades de resolución de problemas mediante ejercicios prácticos
- Establecer una base sólida para conceptos intermedios y avanzados

## 📚 Contenido del Repositorio

### Módulos Completados

#### [01_variables_y_tipos](./01_variables_y_tipos/)
Introducción al sistema de tipos de Python:
- Tipos numéricos: `int`, `float`, `complex`, `bool`
- Tipos de secuencia: `str`, `list`, `tuple`, `range`, `bytes`, `bytearray`, `memoryview`
- Tipos de conjunto: `set`, `frozenset`
- Tipos de mapeo: `dict`
- Tipo nulo: `NoneType`
- Conversión entre tipos (casting)
- Anotaciones de tipo explícitas

#### [02_operadores](./02_operadores/)
Sistema completo de operadores de Python:
- Operadores aritméticos y de asignación
- Operadores de comparación y lógicos
- Operadores de identidad y pertenencia
- Operadores bit a bit
- Operador walrus (`:=`)
- Precedencia y asociatividad de operadores

### Próximos Módulos

- **03_estructuras_control**: Condicionales y bucles
- **04_cadenas**: Métodos y manipulación de strings
- **05_listas_tuplas**: Operaciones avanzadas con secuencias
- **06_diccionarios_sets**: Estructuras de datos no ordenadas
- **07_funciones**: Definición, parámetros y scope
- **08_manejo_archivos**: Lectura y escritura de archivos
- **09_excepciones**: Manejo de errores y excepciones

## 🚀 Requisitos Previos

- **Python**: Versión 3.8 o superior (recomendado 3.11+)
- **Editor de código**: VS Code, PyCharm, o cualquier editor con soporte para Python
- **Conocimientos básicos**: No se requieren conocimientos previos de programación

### Instalación de Python

Descarga Python desde el sitio oficial: [python.org](https://www.python.org/downloads/)

Verifica la instalación:
```bash
python --version
```

## 💻 Uso del Repositorio

### Clonar el Repositorio

```bash
git clone https://github.com/tu-usuario/python-practice.git
cd python-practice
```

### Ejecutar los Archivos

Cada módulo contiene tres archivos principales:

1. **Teoría y ejemplos** (`01_teoria_y_ejemplos.py`):
  ```bash
  python 01_variables_y_tipos/01_teoria_y_ejemplos.py
  ```

2. **Ejercicios** (`02_ejercicios.py`):
   - Abre el archivo en tu editor
   - Completa los ejercicios donde se indica `# Tu código aquí`
   - Ejecuta para verificar:
  ```bash
  python 01_variables_y_tipos/02_ejercicios.py
  ```

3. **Soluciones** (`03_soluciones.py`):
   - Consulta solo después de intentar resolver los ejercicios
  ```bash
  python 01_variables_y_tipos/03_soluciones.py
  ```

### Entorno Virtual (Recomendado)

Aunque este repositorio no requiere dependencias externas, es una buena práctica usar entornos virtuales:

```bash
# Crear entorno virtual
python -m venv venv

# Activar en Windows
venv\Scripts\activate

# Activar en macOS/Linux
source venv/bin/activate

# Desactivar
deactivate
```

## 📐 Convenciones de Código

Este repositorio sigue las convenciones establecidas en PEP 8:

- **Nomenclatura**: `snake_case` para variables y funciones
- **Anotaciones de tipo**: Uso consistente de type hints
- **Comentarios**: Documentación clara y concisa en español
- **Estructura**: Organización lógica con separadores visuales
- **Ejemplos**: Código ejecutable con salida esperada documentada

### Ejemplo de Estilo

```python
# Declaración con anotación de tipo
nombre_usuario: str = "Desarrollador"
edad: int = 25

# Comentarios explicativos
# Los strings son inmutables en Python
mensaje: str = "Hola, mundo"
```

## 🎓 Metodología de Aprendizaje

1. **Lectura teórica**: Estudia el archivo de teoría del módulo actual
2. **Ejecución de ejemplos**: Corre el código para ver los resultados en consola
3. **Práctica independiente**: Resuelve los ejercicios sin consultar las soluciones
4. **Verificación**: Compara tus soluciones con las proporcionadas
5. **Reflexión**: Analiza las diferencias y comprende los conceptos

## 📊 Progreso del Curso

| Módulo | Estado | Ejercicios |
|--------|--------|------------|
| Variables y Tipos | ✅ Completado | 10 |
| Operadores | ✅ Completado | 10 |
| Estructuras de Control | 🔜 Próximamente | - |
| Cadenas | 🔜 Próximamente | - |
| Listas y Tuplas | 🔜 Próximamente | - |
| Diccionarios y Sets | 🔜 Próximamente | - |
| Funciones | 🔜 Próximamente | - |
| Manejo de Archivos | 🔜 Próximamente | - |
| Excepciones | 🔜 Próximamente | - |

## 🤝 Contribuciones

Este es un repositorio de aprendizaje personal. Sin embargo, si encuentras errores o tienes sugerencias:

1. Abre un issue describiendo el problema
2. Proporciona ejemplos claros cuando sea posible
3. Sugiere mejoras específicas

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](./LICENSE) para más detalles.

## 📧 Contacto

Para preguntas o discusiones sobre el contenido:
- GitHub Issues: [Crear un issue](https://github.com/tu-usuario/python-practice/issues)

---

**Nota**: Este repositorio está en desarrollo activo. Los contenidos se actualizan y expanden regularmente.

⭐ Si este repositorio te resulta útil, considera darle una estrella en GitHub.
