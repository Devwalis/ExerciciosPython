import requests



def get_cotacao():
	url = 'https://api.exchangerate-api.com/v4/latest/BRL'

	
	response = requests.get(url)
	data = response.json
		
	if response.status_code == 200:
		
		return data["rates"]
	else:
		print("erro ao obter cotações: ", response.status_code)
		return None
	
	
rates = get_cotacao()
print("USD:", 1 / rates['USD'])
print("EUR:", 1 / rates['EUR'])
print("GBP:", 1 / rates['GBP'])


