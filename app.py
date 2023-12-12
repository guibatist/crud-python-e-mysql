#Crud em Python (Python + MySql)

# Import Biblioteca (pip install mysql-connector-python)
# Conexão com Banco de Dados
import mysql.connector

conexao = mysql.connector.connect(
    host='localhost', #Local do Banco
    user='root', #Usuario 
    password='', #Senha
    database='bancoteste', #Nome do Bacno
)

cursor = conexao.cursor()

# Create - Adicionar informações
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome}", {valor})'
cursor.execute(comando) #Executa o comando determinado na variável "comando"
conexao.commit() #

# Read - Ler linhas e colunas
comando = f'SELECT * FROM vendas'
cursor.execute(comando) #Executa o comando determinado na variável "comando"
resultado = cursor.fetchall() # Ler o banco de dados
print(resultado)


# Update
valor = input("Digite o novo valor")

comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "café"'
cursor.execute(comando) #Executa o comando determinado na variável "comando"



# Delete
comando = f'DELETE FROM vendas WHERE nome_produto = "café"'
cursor.execute(comando) #Executa o comando determinado na variável "comando"
