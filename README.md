Visão Geral: 
O projeto consiste em um conjunto de scripts Python para medir o tamanho de um banco 
de  dados  MySQL  e  ou  tamanho  de  uma  tabela  específica  dentro  do  mesmo.  O  projeto  é 
desenvolvido  para  ser  executado  em  um  ambiente  virtual,  garantindo  que  as  bibliotecas 
necessárias estejam isoladas dentro desse diretório. 
 
Estrutura do Projeto: 
• DataBase.py: Este script é responsável por medir o tamanho total de um banco de 
dados MySQL. 
• Table.py: Este script é responsável por medir o tamanho de uma tabela específica 
dentro de um banco de dados MySQL. 
• config.json: Este arquivo contém as informações de configuração: Host, usuário, 
senha, nome do banco e da tabela a serem usadas pelos scripts. 
 
Configurações: 
Antes de executar os scripts, é necessário configurar as informações no arquivo 
config.json. Este arquivo deve conter as seguintes informações: 
• "host": O endereço IP ou o nome do host do servidor MySQL. 
• "user": O nome de usuário para autenticação no servidor MySQL. 
• "password": A senha para autenticação no servidor MySQL. 
• "database": O nome do banco de dados MySQL que você deseja medir. 
• "table" (opcional): Nome da tabela dentro do banco que você desejar. 
 
Saída: 
• Os scripts retornarão o tamanho do banco de dados ou da tabela especificada em 
megabytes (MB). 
• Se ocorrer um erro, como banco de dados não encontrado ou tabela não 
encontrada, uma mensagem informativa será exibida. 
Considerações de Segurança: 
• As credenciais de acesso ao banco de dados não são incluídas diretamente nos 
scripts, mas sim armazenadas em um arquivo config.json. 
• O ambiente virtual (venv) é utilizado para garantir que as bibliotecas necessárias 
estejam isoladas e não interfiram com o ambiente global do sistema. 
