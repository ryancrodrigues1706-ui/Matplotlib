import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd

meus_dados = pd.DataFrame({ 

'Conjunto de Pizzas': ['Marcelo', 'Dalva', 'Alberto', 'Carlão', 'Cleide', 'Talita', 'Roberto'],
'Quantidade': [5, 10, 3, 7, 2, 6, 1]
}) #Aqui estaremos criando um dataframe com o nome de "meus_dados". Ele funciona como se fosse um repositório de informações.

custom_params = {'axes.spines.right': False, 'axes.spines.top': False} #Aqui criamos uma variável chamada "custom_params" para customizar elementos específicos do gráfico - As bordas, nesse caso.
sns.set_theme(style='ticks', rc=custom_params, palette='flare')  #Aqui escolhemos nosso tema, definindo o estilo, cor e runtime.configuration (rc).

sns.barplot(x=meus_dados['Conjunto de Pizzas'], y=meus_dados['Quantidade']) #Aqui estamos definindo o tipo de gráfico e escolhendo as variáveis ou atributos do "datas" para as colunas "x" e "y".

plt.title('Pizzas', size=22) #Aqui definimos o título do gráfico e o tamanho da fonte dele
plt.legend(title='Quantidade de pizzas que cada casal tem', labels=['Porque eles teriam tantas?'], fontsize=13, title_fontsize=17) #Aqui criamos o título de uma legenda, a legenda em si e os tamanhos de cada um deles

plt.show() #Aqui damos o comando para mostrar o gráfico