accounts = {
    "A1234567": 100,
    "A7654321": 200,
    "A1111111": 300,
    "A2222222": 400,
}

acc = input("Enter account ID: ")

requestAmount = lambda : int(input("Enter amount to withdraw: "))
    
requestOperation = lambda : input("Choose operation: (1) Deposit, (2) Withdraw: ")

checkAccount = lambda : True if acc in accounts else False

deposit = lambda : accounts.update({acc: accounts[acc] + int(input("Enter amount to deposit: "))})

withdraw = lambda amount : accounts.update({acc: accounts[acc] - amount}) if accounts[acc] >= amount else print("Insufficient funds")

checkBalance = lambda : print(accounts[acc])

chooseOperation = lambda operation : deposit() if operation == "1" else withdraw(requestAmount()) if operation == "2" else chooseOperation()

(lambda : chooseOperation(requestOperation()) if checkAccount() else print('Account not found'))()




