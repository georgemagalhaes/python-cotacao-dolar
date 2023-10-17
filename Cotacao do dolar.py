'''
Autor: George Antunes de Abreu Magalhães
Exercício: Cotação do dólar
Disciplina: Requests, Json
Data: 04/12/2022
e-mail: georgemagalhaes@gmail.com
'''

## Para instalar a biblioteca requests => pip install requests
## Para instalar a biblioteca json => pip install json

#!/usr/bin/env python3
import requests
import json

# Versão MS Windows para limpar a tela.
import os
os.system ("cls")

# Versão Linux para limpar a tela.
#import os
#os.system ("clear")

# URL da API de cotação do dólar em relação ao Real
url = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'

# Realiza a requisição GET na URL e extrai a cotação do dólar do JSON
response = requests.get(url)
data = response.json()
dollar_quote = float(data['USDBRL']['bid'])

# Imprime a cotação do dólar
#print(dollar_quote)

# Imprime a cotação do dólar com duas casas decimais
print('{:.2f}'.format(dollar_quote))
