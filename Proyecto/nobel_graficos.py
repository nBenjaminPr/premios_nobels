import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Ruta del archivo

nobel_df = pd.read_csv("C:/Users/Usuario/Desktop/Nico2/Proyectos/Premio_Nobel/data/nobel.csv")

#Que porcetaje de ganadores tiene EEUU por decada?

#Creando columna lugar de nacimiento EEUU
nobel_df['EEUU_born_winner'] = nobel_df['birth_country'] == 'United States of America' 

# Decada
nobel_df ['decade'] = (np.floor(nobel_df['year']/10)*10).astype(int)

#Promedio de cada ganador por decada
prop_usa_winners = nobel_df.groupby('decade', as_index = False)['EEUU_born_winner'].mean()



#Graficas de lineas de los datos

plt.rcParams['figure.figsize'] = [11,7]

ax = sns.lineplot(
    x = 'decade',
    y= 'EEUU_born_winner',
    data= prop_usa_winners
)

plt.title('Proporción de ganadores nacidos en EEUU por década')
plt.xlabel('Década')
plt.ylabel('Proporción')
plt.grid(True)


#Es para imprimir la grafica
plt.show()

