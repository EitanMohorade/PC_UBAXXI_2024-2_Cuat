# Pandas

## Estructura del Apunte

Este apunte se creó originalmente como un Google Colab antes de ser convertido a PDF. Para obtener una versión interactiva, se puede acceder al enlace. Recuerden crear una copia para poder modificar el código y probar.

## ¿Qué es Pandas y para qué sirve?

Pandas es una biblioteca de Python utilizada para el análisis y manipulación de datos. Su estructura principal es el **DataFrame**, una tabla bidimensional similar a una hoja de cálculo. Pandas permite seleccionar, filtrar, agregar y realizar operaciones estadísticas sobre grandes conjuntos de datos.

### Poniendo a punto Pandas

1. Importar Pandas:

   ```python
   import pandas as pd
   pd.__version__
    ```

2. Crear un DataFrame:

```python
    data = {'animal': ['cat', 'cat', 'snake', 'dog'], 'age': [2.5, 3, 0.5, None]}
    labels = ['a', 'b', 'c', 'd']
    df = pd.DataFrame(data, index=labels)
    df
```

3. Mostrar información del DataFrame:

```python
    df.info()
    df.describe()
```

4. Seleccionar columnas y filas:

```python
    df.loc[:, ['animal', 'age']]
    df.iloc[:3]
    df[df['age'].isnull()]
```

5. Filtrar y modificar datos:

```python
    df[df['visits'] > 3]
    df[df['age'].between(2, 4)]
    df.loc['f', 'age'] = 1.5
```

6. Agrupar, sumar y agregar filas:

```python
    df.groupby('animal')['age'].mean()
    df.loc['k'] = ['dog', 5.5, 2, 'no']
    df = df.drop('k')
```

7. Ordenar y transformar columnas:

```python
    df.sort_values(by=['age', 'visits'], ascending=[False, True])
    df['priority'] = df['priority'].map({'yes': True, 'no': False})
```

## Biblioteca de Funciones Pandas

| Función        | Definición                                           | Ejemplo de Uso                       |
|----------------|------------------------------------------------------|--------------------------------------|
| `read_csv()`   | Lee un archivo CSV y lo carga en un DataFrame         | `df = pd.read_csv('data.csv')`       |
| `head()`       | Muestra las primeras filas del DataFrame              | `df.head(7)`                         |
| `info()`       | Muestra información sobre el DataFrame               | `df.info()`                          |
| `describe()`   | Genera estadísticas descriptivas del DataFrame        | `df.describe()`                      |
| `groupby()`    | Agrupa el DataFrame según una o varias columnas       | `df.groupby('columna')`              |
| `value_counts()`| Cuenta valores únicos en una columna                 | `df['columna'].value_counts()`       |
| `sort_values()`| Ordena el DataFrame por columnas                      | `df.sort_values('columna')`          |

## loc vs iloc

* loc accede a los datos por etiquetas.

```python
    df.loc[:, ['nombre', 'edad']]
```

* iloc accede a los datos por posiciones.

```python
df.iloc[:, [1, 3]]
```
