import json
import mysql.connector

def get_table_size(host, user, password, database, table):
    # Conectar ao servidor MySQL
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )

    cursor = connection.cursor(dictionary=True)

    # Obter o tamanho da tabela específica
    query = f"SELECT ROUND(SUM(data_length + index_length) / 1024 / 1024, 2) AS size_mb FROM information_schema.tables WHERE table_schema = '{database}' AND table_name = '{table}'"
    cursor.execute(query)

    table_size = cursor.fetchone()

    # Fechar a conexão
    cursor.close()
    connection.close()

    return table_size['size_mb'] if table_size else None

# Carregar configurações do arquivo JSON
with open('local do arquivo .JSON com as credenciais') as f:
    config = json.load(f)

host = config['host']
user = config['user']
password = config['password']
database_to_measure = config['database']
table_to_measure = config.get('table')  # Lê o nome da tabela do arquivo JSON, se presente

if table_to_measure is None:
    print("Nome da tabela não especificado no arquivo JSON.")
    exit()

size_of_table = get_table_size(host, user, password, database_to_measure, table_to_measure)

if size_of_table is not None:
    print(f"Tamanho da tabela '{table_to_measure}' na DataBase '{database_to_measure}': {size_of_table} MB")
else:
    print(f"Tabela '{table_to_measure}' não encontrada no banco de dados '{database_to_measure}' ou sem dados.")
