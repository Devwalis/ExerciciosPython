import requests



def get_cotacao():
	url = 'https://api.exchangerate-api.com/v4/latest/' + destino

	
	response = requests.get(url)
	data = response.json
		
	if response.status_code == 200:
		
		return data["rates"]
	else:
		print("erro ao obter cotações: ", response.status_code)
		return None
	
def converter_cotacao(origem = 'USD', destino = 'BRL', valor= 1):
	rates = get_cotacao(destino)
	return round(1 / rates['origem'], 4)



def menu():
	print()
	print('1 - Converter Dolar em Real')
	print('2 - Converter Euro em Real')
	print('3 - Converter Libras em Real')
	print('4 - Outra cotação')
	print('0 - Sair')
	print()




opcap = 1


while opcao != 0:
	menu()
	opcao = int(input("Escolha uma opção: "))	
	
	destino = 'BRL'
	valor = input("Digite o valor: ")

	match opcao: 
		case 1: origem = 'USD'

		case 2: origem = 'EUR'

		case 3: origem = 'GBP'		

		case 4: 
			origem = input("Digite a Origem: " )
			destino = input("Digite o Destino: ")
	if opcao:
		print()
		print('***************************************')
		print(f'{origem} para {destino}: ', converter_cotacao(origem))
		print('***************************************')
		print()	


	
