class Categoria:
	def __init__(self, nome):
		self.nome = nome
		

	def detalhar(self):
		return self.__dict__


	def inserir(self):
	
	try: 
		with open('db/Categoria.json') as file:
	except Exception:
		lista = []

	lista.append(self.detalhar())
	
	with open('db/Categoria.json', 'w') as file:
		json.dump(lista, file, ident=4)

	print('Registro cadastrado com sucesso')

		
		
