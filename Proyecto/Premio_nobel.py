import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Ruta del archivo

nobel_df = pd.read_csv("C:/Users/Usuario/Desktop/Nico2/Proyectos/Premio_Nobel/data/nobel.csv")
"""
#Vizualizamos los 5 primeros datos
#print(nobel_df.head())
"""

"""
#Vizualizamos todos los datos del DF
#print(nobel_df.info)
"""

"""
#Que vamos analizar?
#Como conocer el conjunto de forma general
# - Cuantos premios tenemos regitstrados? Existen 911 premios
# - Cuantos premios han ganado hombrey mujeres? Los hombre tienen 836 premios y muejeres 49
# - Que paises han ganado más premios? - Estados unidos tiene más premios ganados 
# - Que categoria tiene más premios? La categoria medicina tiene más premios ganados 211
"""


"""
#Cantidad de Filas
print(len(nobel_df))
"""


"""
#Cantidad de generos
print(nobel_df['sex'].value_counts())
"""

"""
#Vizualiza los 10 paises con más premios nobels
print(nobel_df['birth_country'].value_counts().head(10))
"""

"""
#Vizualiza las categorias con más premios nobels
print(nobel_df['category'].value_counts())
"""