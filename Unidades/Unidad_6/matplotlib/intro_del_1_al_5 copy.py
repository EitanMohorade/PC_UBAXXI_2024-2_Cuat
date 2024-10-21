'''
Para realizar estos ejercicio, debemos importar la información del PBI per cápita de los
distintos países, a lo largo de un período que abarca desde 1952 y 2007.
# Importo la información
url =
"https://raw.githubusercontent.com/plotly/datasets/master/gapminder_with_codes.
csv"
data = pd.read_csv(url)
# Modificar el tipo de dato:
data['year'] = data['year'].astype("int")
data.head()
data.info()
'''