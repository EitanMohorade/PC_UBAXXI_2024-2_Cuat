'''
Elegir un continente el cual te gustaría analizar con más detalle:
# =========== Código de alumno ===============
continent =
# ============================================
data_one_continent = data[data["continent"] == continent]
data_one_continent = data_one_continent[['country', 'gdpPercap']]
data_one_continent = data_one_continent.groupby(['country']).agg('sum')
data_one_continent = data_one_continent.sort_values(by=['gdpPercap'])
data_one_continent[['gdpPercap']]
Realizar un gráfico de barras horizontales que muestre el PBI per cápita de los habitantes del
continente escogido (columna gdpPercap).
El gráfico debe tener:
● Título apropiado
● Nombre y unidades de los ejes cartesianos en caso de ser necesario
● Nombre de los paises al lado de cada barra
● Grilla con líneas verticales únicamente, color "#CDD7DA" y línea discontinua.
fig, ax = plt.subplots()
# =========== Código de alumno ===============
# ============================================
plt.show()

'''