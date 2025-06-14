import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Ruta del archivo

nobel_df = pd.read_csv("C:/Users/Usuario/Desktop/Nico2/Proyectos/Premio_Nobel/data/nobel.csv")

#Vizualizamos los 5 primeros datos
#print(nobel_df.head())

#Vizualizamos todos los datos del DF
#print(nobel_df.info)

#Que vamos analizar?
#Como conocer el conjunto de forma general
# - Cuantos premios tenemos regitstrados?
# - Cuantos premios han ganado hombrey mujeres?
# - Que paises han ganado más premios?
# - Que categoria tiene más premios?

"""
#Cantidad de Filas
print(len(nobel_df))
"""

print(nobel_df['sex'].value_counts())