import matplotlib.pyplot as plt
from moedas import converter_cotacao


cotacoes = getcotacao()

#Criar lista de moedas 

l_moedas = ['USD -Dólar', 'EUR - Euro', 'GBP - Libras']
l_valores = [1 / cotacoes['USD'], 1 / cotacoes['EUR'], 1 / cotacoes['GBP']]



