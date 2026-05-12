class Produto:
	
	def __init__(self, nome, valor, quantidade = 0, marca = ''):
		
		self.nome = ''
		self.marca =''
		self.quandtidade = quantidade
		self.model = ''
		self.valor = ''
		

	def vender(self, quantidade):
		if(quantidade > self.quantidade):
		print("não há estoque suficiente")
		print("Quantidade máxima:" , self.quantidade)
		self.quantidade -= quantidade

	def comprar(self , quantidade):
		self.quantidade += quantidade	
	

produto = Produto('Celular', 2000, 100, 'Samsung', 'J8')

produto1 = Produto('Geladeira',4000, 50, 'Brastemo', 'BST900')


print(produto0.__dict__)
print(produto1.__dict__)
print(produto2.__dict__)



