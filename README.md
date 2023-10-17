# python-cotacao-dolar

a) Este código foi escrito no ambiente MS Windows, portanto, se ele for utilizado no Linux é necessário fazer a conversão do arquivo:
> dos2unix [nome do arquivo].py

b) Caso o código seja utilizado para monitorar a cotação do dólar no Zabbix, é possível que quando for configurado o "item" retorne um erro de permissão "Permissiona Denied". 
Então, deve ser dada a permissão de leitura ao arquivo utilizando o comando CHMOD, por exemplo:
> chmod 777 [nome do arquivo].py
