'''
A continuación vamos a agrupar PBI per capita por continente.
data_continent = data[['continent', 'gdpPercap']]
data_continent = data_continent.groupby(['continent']).agg('sum')
data_continent
Realizar un gráfico de torta la proporción del PBI per cápita de los habitantes de cada
continente (columna gdpPercap).
El gráfico debe tener:
● Título apropiado
● Cada parte con el nombre del continente y el porcentaje redondeado a las décimas.
● El color de cada parte será:
○ América: "#30BFDE"
○ Asia: "#E31E4B"
○ África: "#E36F1E"
○ Oceanía: "#1EE39B"
○ Europa: "#1E92E3"
fig, ax = plt.subplots()
# =========== Código de alumno ===============
# ============================================
plt.show()
'''