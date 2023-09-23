bank_account_balances1 = [5322.0, 577.35, -100.0]
bank_account_balances2 = [322.0, 8577.35, -80.0]

# Funktionen sind dafür da, um einmalig was zu definieren, um sie dann immer wieder verwenden zu können ohne andaurent den Code nochmal zu scheiben zu müssen.
def print_bank_account_info(bank_account_info):
    for balance in bank_account_info:
        print(balance)

# um die Funktion ausführen zu können, müssen wir sie ein Mal hinschreiben und derren Paramete definieren
print_bank_account_info(bank_account_balances1)
print_bank_account_info(bank_account_balances2)