import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Ruta del archivo
nobel_df = pd.read_csv("C:/Users/Usuario/Desktop/Nico2/Proyectos/Premio_Nobel/data/nobel.csv")

nobel_df['female_winner'] = nobel_df['sex'] == 'Female' 

# Decada
nobel_df ['decade'] = (np.floor(nobel_df['year']/10)*10).astype(int)

#Agrupación de mujeres ganadas
prop_famele_winner = nobel_df.groupby(['decade', 'category'], as_index = False)['female_winner'].mean()


plt.rcParams['figure.figsize'] = [11,7]

ax = sns.lineplot(
    x = 'decade',
    y= 'female_winner',
    data= prop_famele_winner,
    hue= 'category'
)

plt.title('Proporción de ganadores de mujeres por década')
plt.xlabel('Década')
plt.ylabel('Proporción')
plt.grid(True)

#Es para imprimir la grafica
plt.show()

