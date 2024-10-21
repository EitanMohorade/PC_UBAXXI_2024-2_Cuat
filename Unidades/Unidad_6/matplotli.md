# Matplotlib

## ¿Qué es Matplotlib?

Matplotlib es una biblioteca de Python ampliamente utilizada para crear gráficos de alta calidad que pueden ser compartidos o publicados. A continuación, veremos los usos más comunes de matplotlib.

## Pyplot

`pyplot` proporciona una interfaz para matplotlib, diseñada al estilo de Matlab. Vamos a explorar las instrucciones más importantes con ejemplos interactivos.

### Primer gráfico

```python
    import matplotlib.pyplot as plt
    x = [0, 2, 10, 11, 18, 25]
    y = [0, 1, 2, 3, 4, 5]
    plt.plot(x, y)
    plt.show()
```

## Diferencias entre plt.figure() y plt.subplots()

* plt.figure() crea una figura vacía sin axes.
* plt.subplots() crea una figura con axes, permitiendo mayor control sobre el gráfico.

## Partes de una Figura

Una figura es el marco donde se trazan gráficos, mientras que los "axes" son las áreas donde se especifican puntos en coordenadas. No confundir "axes" con "axis", que son los ejes cartesianos que definen límites y escalas.

## Modificar el aspecto de un gráfico

Puedes cambiar el color, tipo de línea, grosor, y marcadores de un gráfico.

```python
    ax.plot(x, y, color='green', marker='^', linestyle='--', markersize=8, linewidth=1.2)
```

## Grilla

Para facilitar la lectura de un gráfico, puedes agregar una cuadrícula con ax.grid().

## Títulos y Etiquetas

Para añadir títulos y etiquetas a los ejes:

```python

    ax.set_title("Gráfico de posición")
    ax.set_xlabel('Tiempo (min)')
    ax.set_ylabel('Distancia (m)')
```

## Leyendas

Para gráficos con varias líneas, añade una leyenda con ax.legend().

## Tipos de Gráficos

* Gráfico de Línea: Muestra cambios en un rango continuo.
* Gráfico de Dispersión: Muestra la relación entre dos variables.
* Gráfico de Barras: Compara proporciones.
* Gráfico de Torta: Muestra proporciones como parte de un todo.

## Gráficos Múltiples

Puedes crear gráficos con varias curvas en un solo gráfico o múltiples gráficos en una grilla usando subplots().

## Conclusión

Matplotlib ofrece una gran flexibilidad y control para la creación de gráficos en Python. Con pyplot, puedes crear desde gráficos simples hasta visualizaciones complejas ajustando los parámetros y funciones adecuadas.
