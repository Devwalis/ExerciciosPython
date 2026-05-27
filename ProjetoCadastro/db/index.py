from ProjetoCadastro.Produto import Produto


def menu():
	print()
	print("1 - Listar Produtos")
	print("2 - Inserir Produto")
	print("3 - Alterar Produto")
	print("4 - Excluir Produto")
	print("0 - Sair")
	print()

opcao = 1

while opcao != 0:
	menu()
	opcao = int(input('Escolha uma opção: '))
	
	
	match opcao:
		case 1:
			print('****************************')
			Produto.listarTodos()
			print('****************************')
			
		case 2:
			codigo = input('Digite o código: ')
			nome = input('Digite o nome: ')
			quantidade = input('Digite a quantidade: ')
			valor = input('Digite o valor do produto: ')

			produto = Produto(codigo, nome, quantidade, valor)
			
			produto.inserir()


		case 3:
			Produto.alterar()

		case 4:
			Produto.excluir()
