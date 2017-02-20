#JWLS 12/02/17
#Title-Buscando preco do pescado na ceasa recife

import requests
from bs4 import BeautifulSoup

#usando BeautifulSoup para tratar os dados

with open('data1_pesca.html', 'r') as aq:
	soup = BeautifulSoup(aq, 'lxml')

#1-passo: Separar o nome dos arquivos a serem pesquisados 

string_data = soup.find_all('option')  #Delimitou o campo de busca dos nomes dos arquivos
n = len(string_data)                   #Comprimento do vetor string_data
name_data = []                        #Nomes dos dados a serem utilizados
cont = 1

while  cont < n:
	x = str(string_data[cont])
	y = str(x[15:34])
	name_data.append(y)
	cont += 1


with open('name_data.txt','w') as arquivo:
	for i in xrange(len(name_data)):
		arquivo.write(name_data[i])

#2-passo: Utilizar o requests para buscar todos os arquivos

f = open("data_ceasa.txt","wr")

f.write("Data\t")
f.write("Ambiente\t")
f.write("Unidade\t")
f.write("Proced\t")
f.write("Especies\t")
f.write("PrecoMin\t")
f.write("PrecoCom\t")
f.write("PrecoMax\t")
f.write("Situacao\n")


for j in xrange(len(name_data)):

	d = name_data[j]
	dat = (d[9:15]).encode('utf8')
	data = str(dat)
	
	url = 'http://ceasape.org.br/verCotacao.php?tipo=pescados' 
	payload = {'arquivo_anterior':name_data[j],
	           'arquivo_anterior':name_data[j],
	           'Submit':'Consultar'}

	r = requests.post(url,data=payload)    #faz a requisicao dos dados para cada data

	with open('data1_pesca.html', 'w') as arq:
		arq.write(r.text.encode('utf-8'))

	#limpando os dados

	soup = BeautifulSoup(r.text, 'lxml')

	tabela = soup.find('table',{'id':'minhaTabela'}) #encontra a tag tabela
	#print(tabela)

	linha_tr = tabela.find_all('tr') #Seleciona todas as linhas da tabela 

	#print(linha_tr)
	
	cont = 1
	while cont <= (len(linha_tr)-3):
		linha1 = [linha_tr[cont].text]   #seleciona cada linha
		variaveis = (linha1[0].split())  #separa cada string por espacos 
		#print(variaveis)

		for i in xrange(len(variaveis)):         #Extrai as informacoes das variaveis
			if variaveis[i] == 'Kg' or variaveis[i] == 'Cx.25Kg':
				ambiente = variaveis[i-1].encode('utf8')
				unidade = variaveis[i].encode('utf8')
				proced = variaveis[i+1].encode('utf8')
				peixe = variaveis[i+2].encode('utf8')
				precoMin = variaveis[i+3].encode('utf8').replace(",",".")
				precoComun = variaveis[i+4].encode('utf8').replace(",",".")
				precoMax = variaveis[i+5].encode('utf8').replace(",",".")
				try:
					situacao = variaveis[i+6].encode('utf8')
				except IndexError:
					situacao = 'Erro'
				f.write('%s\t'%data)
				f.write('%s\t'%ambiente)
				f.write('%s\t'%unidade)
				f.write('%s\t'%proced)
				f.write('%s\t'%peixe)
				f.write('%s\t'%precoMin)
				f.write('%s\t'%precoComun)
				f.write('%s\t'%precoMax)
				f.write('%s\n'%situacao)
				
		cont += 1

f.close()