from datetime import datetime


def formatarData(data = datetime.now(), formato = '%d/%m/%y'):
	return datatime.strftime(data, '%d/%m/%y')

def criarData(data, formato = '%Y-%m-%d'):
	return datetime.strptime(data, formato)


