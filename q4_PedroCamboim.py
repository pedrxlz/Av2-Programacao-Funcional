import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0000",
)

cursor = connection.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS GameStore")

cursor.execute("USE GameStore")

create_users_table = lambda : cursor.execute("CREATE TABLE IF NOT EXISTS USUARIOS (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), console VARCHAR(255))") 

insert_user = lambda nome, console: cursor.execute(f"INSERT INTO USUARIOS (nome, console) VALUES ('{nome}', '{console}')")

remove_user = lambda id_usuario: cursor.execute(f"DELETE FROM USUARIOS WHERE id = {id_usuario}") 

get_users = lambda : cursor.execute("SELECT * FROM USUARIOS") or [print(user) for user in cursor.fetchall()]

create_games_table = lambda : cursor.execute("CREATE TABLE IF NOT EXISTS JOGOS (id INT AUTO_INCREMENT PRIMARY KEY, nome VARCHAR(255), data_lancamento DATE)") 

insert_game = lambda nome, data_lancamento: cursor.execute(f"INSERT INTO JOGOS (nome, data_lancamento) VALUES ('{nome}', '{data_lancamento}')") 

remove_game = lambda id_jogo: cursor.execute(f"DELETE FROM JOGOS WHERE id = {id_jogo}") 

get_games = lambda : cursor.execute("SELECT * FROM JOGOS") or [print(game) for game in cursor.fetchall()]

create_users_table()
create_games_table()

insert_user("João", "Xbox")
insert_game("The Legend of Zelda", "2022-05-20")

get_users()
get_games()

connection.close()
