#Criando um grafico de pizza

#Dados para Plotar
salaries = [1215, 1221, 1263, 1267, 1271, 1274, 1275, 1318, 1320, 1324, 1324, 1326, 1337, 1346, 1354, 1355, 1364, 1367, 1372, 1375, 1376, 1378, 1378, 1410, 1415, 1415, 1418, 1420, 1422, 1426, 1430, 1434, 1437, 1451, 1454, 1467, 1470, 1743, 1477, 1479, 1480, 1514, 1516, 1522, 1529, 1544, 1547, 1554, 1562, 1584, 1595, 1616, 1626, 1717]

import numpy as np

#Chamamos a função histogram() para criar intervalo de $50
count, labels = np.histogram(salaries, bins=np.arange(1100, 1900, 50))

#list comprehension para obter elementos vizinhos
labels = ['$'+str(labels[i])+'-'+str(labels[i+1]) for i, _ in enumerate(labels[1:])]

#Tirando os intervalos = 0 
non_zero_pos = [i for i, x in enumerate(count) if x !=0]

#Utilizamos o non_zero_pos para filtrar count e labels excluindo os elementos vazios
labels = [e for i, e in enumerate(labels) if i in non_zero_pos]
count = [e for i, e in enumerate(count) if i in non_zero_pos]

#Criamos a vizualização do grafico de pizza

from matplotlib import pyplot as plt
plt.pie(count, labels=labels, autopct='%1.1f%%')
plt.title('Monthly salaries in the Sales Department')
plt.show()
