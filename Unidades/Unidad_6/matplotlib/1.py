'''
Elegir un año en el que desees ver la relación entre la expectativa de vida de los habitantes
(columna `lifeExp`) y el PBI per cápita de los habitantes (columna gdpPercap).
# Modifica este valor
# =========== Código de alumno ===============
year =
# ============================================
data_year = data[data["year"] == year]
data_year.head()
Realizar un gráfico de puntos que muestre la relación entre la expectativa de vida (columna
lifeExp) y el PBI per cápita de los habitantes (columna gdpPercap).
El gráfico debe tener:
● Título apropiado
● Nombre y unidades de los ejes cartesianos
● Marcador de tipo triangular y color "#23A763"
● Grilla
fig, ax = plt.subplots()
# =========== Código de alumno ===============
# ============================================
plt.show()
'''