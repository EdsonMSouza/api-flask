import pandas as pd
from flask import Flask, jsonify

# inicializa o Flask
app = Flask(__name__)

# Criando uma rota para acesso ao site (aplicação)
@app.route('/') # decorator (define uma rota)
def homepage():
  retorno = 'A API está online.</br>'
  retorno += '<h3>Métodos da API</h3>'
  retorno += '<em>/somar/v1/v2</em> - Retorna a soma entre dois valores v1 e v2</br>'
  retorno += '<em>/multiplicar/v1/v2</em> - Retorna a multiplicação entre dois valores v1 e v2</br>'
  retorno += '<em>/previa</em> - Retorna os cinco primeiros registros de um <em>dataset</em> sobre vendas</br>' 
  retorno += '<em>/totalvendas</em> - Retorna o total das vendas de um <em>dataset</em> sobre vendas</br>'
  return retorno
  
## Construindo duas funcionalidades de calculadora (somar e multiplicar)

# Somar
@app.route('/somar/<string:v1>/<string:v2>')
def somar(v1, v2):
  retorno = {'operacao':'adição', 'v1':v1, 'v2':v2,'resultado':int(v1)+int(v2)}
  return jsonify(retorno)

# Multiplicar
@app.route('/multiplicar/<string:v1>/<string:v2>')
def multiplicar(v1, v2):
  retorno = {'operacao':'multiplicação', 'v1':v1, 'v2':v2,'resultado':int(v1)*int(v2)}
  return jsonify(retorno)

# Acessando dados de um dataset (Pandas)
# Listando os cinco primeiros registros da tabela
@app.route('/previa') 
def previa():
  dados = pd.read_csv('https://www.edsonmelo.com.br/src/dados/vendas.csv')
  resposta = dados.head(5).to_dict(orient="list")
  return jsonify(resposta)
  
# Acessando dados de um dataset (Pandas)
# Mostrando o Total de Vendas do Dataset
@app.route('/totalvendas')
def vendas():
  dados = pd.read_csv('https://www.edsonmelo.com.br/src/dados/vendas.csv')
  resposta = {'total_vendas':dados.Vendas.sum()}
  return jsonify(resposta)
  
# executando a aplicação de modo aberto (web)
app.run('0.0.0.0', debug=True)
