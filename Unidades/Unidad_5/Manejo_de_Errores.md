# Manejo de Errores

## Introducción al Manejo de Errores

El manejo de errores es fundamental en el desarrollo de software, especialmente al trabajar con datos, donde los errores son inevitables. En el ámbito de Analítica de Datos, se invierte una gran cantidad de tiempo en la depuración de errores, lo que puede representar hasta un tercio del tiempo total de un proyecto.

### Importancia de la Validación de Ingreso

- **Frecuencia de Errores**: La entrada de datos es uno de los puntos más críticos donde ocurren errores.
- **Estrategias para Reducir Errores**:
  - Simplificar formatos de datos.
  - Validar ingresos para detectar y corregir errores.

### Recomendaciones para la Validación

1. Validar siempre que sea posible y que tenga sentido en términos de costo-beneficio.
2. Ejemplos de validación incluyen verificar rangos de edad y formatos de entrada.

## Manejo de Excepciones

Las excepciones son eventos que interrumpen el flujo normal del programa. Python ofrece varias excepciones incorporadas y permite crear excepciones personalizadas.

### Ejemplo Común de Excepciones

| Excepción        | Causa del error                            |
|------------------|-------------------------------------------|
| `AssertionError` | Falla `assert`.                           |
| `AttributeError` | Referencia de atributos fallida.         |
| `EOFError`       | Fin de archivo alcanzado.                 |
| `ValueError`     | Conversión de tipo fallida.              |

### Estructura try/except

El bloque `try` se utiliza para intentar ejecutar código que puede fallar, y el bloque `except` captura las excepciones que se producen.

```python
try:
    # Código que puede fallar
except:
    # Manejo de la excepción
```

## Uso de else y finally

else: Se ejecuta si no ocurre una excepción en el bloque try.
finally: Siempre se ejecuta, independientemente de si ocurrió una excepción.
Ejemplo con finally

```python

    def probar_finally():
        try:
            return 2
        finally:
            print("Código del bloque finally")
```

## Cláusula raise

raise se utiliza para lanzar excepciones personalizadas cuando se produce una condición específica.

```python

if x > 5:
    raise Exception(f'No debe exceder 5. El valor es: {x}.')
```

## Ejemplo Práctico

Ejercicio: Crear una función que calcule el cociente entre dos números, manejando excepciones adecuadamente.

```python

def calcular_division(x, y):
    try:
        cociente = x / y
    except ZeroDivisionError:
        print("Error: División por cero.")
    else:
        print(f"El cociente es: {cociente}")
    finally:
        print("Ejecutando bloque finally.")
```

```css

Este formato resalta los puntos clave y mantiene la estructura lógica del contenido original. Si necesitas agregar más detalles o modificar algo, ¡dímelo!
```
