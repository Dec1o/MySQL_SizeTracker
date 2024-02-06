import json
import mysql.connector

def get_database_size(host, user, password, database):
    # Conectar ao servidor MySQL
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )

    cursor = connection.cursor(dictionary=True)

    # Obter o tamanho do banco de dados
    query = f"SELECT ROUND(SUM(data_length + index_length) / 1024 / 1024, 2) AS size_mb FROM information_schema.tables WHERE table_schema = '{database}'"
    cursor.execute(query)

    database_size = cursor.fetchone()

    # Fechar a conexão
    cursor.close()
    connection.close()

    return database_size['size_mb'] if database_size else None

# Carregar configurações do arquivo JSON
with open('C:/Users/DécioCarvalhoFariaFa/VsCode/TAM_Banco/venv/config.json') as f:
    config = json.load(f)

host = config['host']
user = config['user']
password = config['password']
database_to_measure = config['database']

size_of_database = get_database_size(host, user, password, database_to_measure)

if size_of_database is not None:
    print(f"Tamanho da DataBase '{database_to_measure}': {size_of_database} MB")
else:
    print(f"Banco de dados '{database_to_measure}' não encontrado ou sem tabelas.")
