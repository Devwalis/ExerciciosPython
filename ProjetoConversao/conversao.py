import requests



def get_cotacao():
	url = 'https://api.exchangerate-api.com/v4/latest/BRL'

	
	response = requests.get(url)
	data = response.json

	print(data)
get_cotacao()

