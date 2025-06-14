import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Ruta del archivo
nobel_df = pd.read_csv("C:/Users/Usuario/Desktop/Nico2/Proyectos/Premio_Nobel/data/nobel.csv")

#Transformamos fechas de objeto a int
nobel_df['birth_date'] = pd.to_datetime(nobel_df['birth_date'])

#Columna booleana
nobel_df['año'] = nobel_df['year'] - nobel_df['birth_date'].dt.year


#Infor de la persona mas joven en ganar un premio nobel
persona_mas_joven = nobel_df.loc[nobel_df['año'].idxmin()]


#Grafica por año y edad
ax = sns.lmplot(
    x = 'year',
    y= 'año',
    data= nobel_df,
    aspect=2,
    line_kws = {'color': 'Black'}
    )

plt.title('Proporción de ganadores de mujeres por década')
plt.xlabel('Year')
plt.ylabel('Edad')
plt.grid(True)

plt.show()

