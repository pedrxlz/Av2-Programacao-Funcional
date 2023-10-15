
requestLogin = lambda : input("Digite o login: ")
requestPassword = lambda : input("Digite a senha: ")
requestOption = lambda : input("Escolha uma opção: (1) Cadastrar Usuário, (2) Fazer Login: ")

matchUser = lambda file, login, password: True if any([True for linha in file if login == linha.strip().split(':')[0] and password == linha.strip().split(':')[1]]) else False

register = lambda : (lambda login = requestLogin(), password = requestPassword(): (lambda file = open('users.txt', 'a'): file.write(f"{login}:{password}\n") and print("Usuário cadastrado com sucesso!"))())()

login = lambda : (lambda login = requestLogin(), password = requestPassword(): (lambda file = open('users.txt', 'r'): (lambda: print("SUCESSO") if matchUser(file, login, password) else print("FRACASSO"))())())()

(lambda option = requestOption(): register() if option == "1" else login() if option == "2" else print("Opção inválida."))()


