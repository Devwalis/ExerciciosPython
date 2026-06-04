import matplotlib.pyplot as plt
from moedas import converter_cotacao


cotacoes = getcotacao()

#Criar lista de moedas 

l_moedas = ['USD -Dólar', 'EUR - Euro', 'GBP - Libras']
l_valores = [1 / cotacoes['USD'], 1 / cotacoes['EUR'], 1 / cotacoes['GBP']]

#Função para criar gráfico em barra

def grafico_barra(1_moedas, 1_valores):
	plt.bar(1_moedas, 1_vaores)
	plt.title('Converões para real (BRL')
	plt.xlabel('Moedas')
	plt.ylabel('BRL (R$)')
	Plt.show()

#Função para criar gráfico de pizza


def exibir_grafico_pizza(moedas, valores):
	plt.pie(valores, labels=moedas, autopct="%1.1f%%")
	plt.title("Proporção das moedas em relação ao real")
	plt.show()

	
