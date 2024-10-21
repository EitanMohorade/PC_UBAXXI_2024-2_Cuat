'''
. A continuación verá todos los países de los que poseemos información. Eligir uno que no
sea nuestro país y luego, crear un nuevo DataFrame.
data["country"].unique()
# =========== Código de alumno ===============
country =
# ============================================
data_country = data[data["country"] == country]
data_country.head()
Realizar un gráfico de línea que muestre el PBI per cápita de los habitantes de Argentina
(columna gdpPercap) a lo largo del tiempo y del país escogido anteriormente:
El gráfico debe tener:
● Título apropiado
● Nombre y unidades de los ejes cartesianos
● Linea sólida, espesor 2.2 y color "#30BFDE" para la curva de nuestro país.
● Linea sólida, espesor 2.2 y color "#1E92E3" para la curva del nuevo país.
● Referencias
● Grilla
fig, ax = plt.subplots()
# =========== Código de alumno ===============
# ============================================
plt.show()
'''