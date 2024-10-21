# Archivos

## Introducción

Los archivos son estructuras de datos persistentes que permiten conservar y compartir información entre usuarios y procesos. Son esenciales en la programación para guardar y recuperar datos de manera persistente.

## Interacción con Archivos en Python

Python ofrece la función `open()` para abrir archivos y establecer un vínculo entre el archivo y el programa. El archivo se manipula a través de un alias que apunta a la posición inicial del archivo en la memoria interna.

### Sintaxis de `open()`

```python
    alias = open(nombre_completo_archivo, modo)
```

## Modos de Apertura

* r (read): Lectura del archivo.
* w (write): Escritura, sobreescribe el archivo.
* a (append): Añadir contenido al final del archivo.
* r+: Lectura y escritura sin eliminar el contenido previo.
* w+: Lectura y escritura, borra el contenido del archivo al abrir.

## Operaciones de Lectura y Escritura

* read(): Lee todo el archivo y lo devuelve como una cadena de texto.
* readlines(): Lee cada línea del archivo y las devuelve en una lista.
* readline(): Lee una línea a la vez.
* write(): Escribe un string en el archivo.
* writelines(): Escribe una lista de strings en el archivo.
Ejemplo de uso:

```python

    archivo = open("archivo.txt", "w")
    archivo.write("hola\n")
    archivo.write("adios\n")
    archivo.close()
```

## Manejo de Buffers

El sistema operativo usa buffers para gestionar la lectura y escritura de archivos, lo que permite la manipulación de grandes volúmenes de datos en bloques, en lugar de hacerlo dato por dato.

## Archivos Planos

Los archivos de texto plano (.txt) son el tipo más simple de archivo. También se pueden trabajar archivos CSV (.csv), que permiten almacenar datos estructurados, separados por comas o puntos y comas.

Ejemplo de manejo de archivos CSV:

```python

    completo = open('datosCompletos.csv', 'w')
    datos = open('datos1.csv')
    lineas = datos.readlines()
    datos.close()

    for linea in lineas:
        linea = linea.strip('\n').split(';')
        linea[3] = int(linea[3])  # Convierte el puntaje a entero
        completo.writelines(linea)
    completo.close()
```

## Cierre de Archivos

Es importante cerrar los archivos con close() para liberar los recursos y garantizar que toda la información se guarde correctamente.

Manejo Seguro con with
Usar with open asegura que el archivo se cierre automáticamente cuando el bloque de código termina su ejecución.

```python

    with open('archivo.txt', 'r') as archivo:
        contenido = archivo.read()
```

```python
    Este resumen organiza los puntos clave en secciones y mantiene ejemplos de código relevantes para mayor claridad.
```
