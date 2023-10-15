accounts = {
    "A1234567": 100,
    "A7654321": 200,
    "A1111111": 300,
    "A2222222": 400,
}

acc = input("Digite o Id da conta: ")

requestAmount = lambda : int(input("Digite o valor para transferir: "))
    
requestOperation = lambda : input("Escolha uma opção: (1) Deposito, (2) Transferencia: ")

checkAccount = lambda : True if acc in accounts else False

deposit = lambda : accounts.update({acc: accounts[acc] + int(input("Digite o valor para transferir: "))})

withdraw = lambda amount : accounts.update({acc: accounts[acc] - amount}) if accounts[acc] >= amount else print("Saldo insuficiente")

checkBalance = lambda : print(accounts[acc])

chooseOperation = lambda operation : deposit() if operation == "1" else withdraw(requestAmount()) if operation == "2" else chooseOperation()

(lambda : chooseOperation(requestOperation()) if checkAccount() else print('Conta nao encontrada'))()




