'''
Para estos ejercicios, vamos a crear valores aleatorios, que serán contenidos en un
DataFrame que llamaremos df:
np.random.seed(0)
df = pd.DataFrame(data={'a':np.random.randint(0, 100, 50),
'b':np.random.randint(0, 100, 50),
'c':np.random.randint(0, 100, 50),
'd':np.random.randint(0, 100, 50)})
df.head()
'''