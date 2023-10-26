#Plotando dados do Pandas com um grafico de barras

import pandas as pd
import matplotlib.pyplot as plt

#Preparando o DataFrame
us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")
top_us_cities = us_cities[us_cities.Population.ge(1000000)]
top_cities_count = top_us_cities.groupby(['State'], as_index = False).count().rename(columns={'City': 'cities_count'})[['State','cities_count']]

#Desenhando o grafico
top_cities_count.plot.bar('State', 'cities_count', rot=0)
plt.xlabel("States")
plt.ylabel("Top cities count")
plt.title("Number of Megacities per US State")
plt.yticks(range(min(top_cities_count['cities_count']), max(top_cities_count['cities_count'])+1))
plt.show()
