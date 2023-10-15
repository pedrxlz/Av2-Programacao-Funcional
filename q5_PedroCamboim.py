from flask import Flask, redirect, render_template_string, request

# Q1
accounts = {
    "A1234567": 100,
    "A7654321": 200,
    "A1111111": 300,
    "A2222222": 400,
}

checkAccount = lambda account_number : True if account_number in accounts else False

deposit = lambda account_number, amount : accounts.update({account_number: accounts[account_number] + int(amount)})

withdraw = lambda account_number, amount : accounts.update({account_number: accounts[account_number] - amount}) if accounts[account_number] >= amount else 'Saldo Insuficiente'

checkBalance = lambda account_number : accounts[account_number]


app = Flask(__name__)

accounts_template = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Selecione uma conta</title>
        </head>
        <body>
            <h1>Selecione uma conta e ação:</h1>
            <form method="post">
                <select name="account">
                    {% for account_number, _ in accounts.items() %}
                    <option value="{{ account_number }}">{{ account_number }}</option>
                    {% endfor %}
                </select>
                <select name="action">
                    <option value="deposit">Depósito</option>
                    <option value="withdraw">Saque</option>
                    <option value="balance">Saldo</option>
                </select>
                <input type="submit" value="Selecionar">
            </form>
        </body>
        </html>
"""

deposit_template = '''
         <form method="POST">
             <section style="display: flex; justify-content: center">
                 <div style="display: flex; flex-direction: column; gap: 5px; max-width: 350px; width: 100%">
                    <h1>Insira o valor a depositar: </h1>
                    <label for="amount">Quantia a depositar: </label>
                    <input id="amount" type="number" name="amount" placeholder="$0.00" type="number">
                    <input type="submit">
                 </div>
             </section>
         </form>
     '''

withdraw_template = '''
            <form method="POST">
                <section style="display: flex; justify-content: center">
                    <div style="display: flex; flex-direction: column; gap: 5px; max-width: 350px; width: 100%">
                        <h1>Insira o valor a sacar: </h1>
                        <label for="amount">Quantia a sacar: </label>
                        <input id="amount" type="number" name="amount" placeholder="$0.00" type="number">
                        <input type="submit">
                    </div>
                </section>
            </form>
        '''

balance_template = '''
            <section style="display: flex; justify-content: center">
                <div style="display: flex; flex-direction: column; gap: 5px; max-width: 350px; width: 100%">
                    <h1>Saldo</h1>
                    {{balance}}
                </div>
            </section>
        '''


render_accounts_page = lambda : render_template_string(accounts_template, accounts = accounts)
render_deposit_page = lambda : render_template_string(deposit_template)
render_withdraw_page = lambda : render_template_string(withdraw_template)
render_balance_page = lambda account_number: render_template_string(balance_template, balance = accounts[account_number])

handle_deposit = lambda account_number: deposit(account_number, int(request.form['amount'])) or redirect(f'/{account_number}/balance')
handle_withdraw = lambda account_number: withdraw(account_number, int(request.form['amount'])) or redirect(f'/{account_number}/balance')


app.add_url_rule(rule= '/', endpoint='index', view_func = lambda: redirect(f'/{request.form['account']}/{request.form['action']}') if request.method == 'POST' else render_accounts_page(), methods=['GET', 'POST'])
app.add_url_rule(rule= '/<account_number>/deposit', endpoint='deposit', view_func = lambda account_number: handle_deposit(account_number) if request.method == 'POST' else render_deposit_page(), methods=['GET', 'POST'])
app.add_url_rule(rule= '/<account_number>/withdraw', endpoint='withdraw', view_func = lambda account_number: handle_withdraw(account_number) if request.method == 'POST' else render_withdraw_page(), methods=['GET', 'POST'])
app.add_url_rule(rule= '/<account_number>/balance', endpoint='balance', view_func = lambda account_number: render_balance_page(account_number), methods=['GET', 'POST'])

app.run(debug=True)




