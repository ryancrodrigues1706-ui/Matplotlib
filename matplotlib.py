import matplotlib.pyplot as plt
import numpy as np
#Gráfico 1
x = np.array([0, 1, 2, 3]) #Define os pontos do gráfico do eixo X.
y = np.array([3, 8, 1, 10]) #Define os pontos do gráfico do eixo Y.

plt.subplot(1,2,1) #Define o número de linhas horizontais, colunas e a posição do gráfico.

plt.title('Gráfico de linha') #Serve para definir um título ao gráfico correspondente.
plt.grid(color='black', linewidth=0.5, linestyle='-')#Esse comando serve para adicionar uma grade de fundo.

plt.plot(x,y, marker = 'o', color = 'red') #Aqui ele irá "plotar" os "arrays" que você definiu nos pontos x e y, você também pode adicionar configurações como cor, tipo de linha e marcadores.

#Depois de já ter "plotado um gráfico", é possível criar um novo gráfico dentro da mesma imagem.
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])


plt.subplot(1, 2, 2)

plt.grid(color='black', linewidth=0.5, linestyle='-')

plt.title('Gráfico de Dispersão')
plt.scatter(x,y)
plt.savefig("C:/Users/Aluno 02/Downloads/Meu gráfico.png")

plt.show() #Esse comando serve para visualizar os gráficos que você definiu anteriormente.