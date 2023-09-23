myAge = 26

myResult = myAge * 2

# Loops führen eine Anweisung mehrmals durch. Hier wird fünf Mal iteriert
# 52 * 2 = 102 * 2 = 204 * 2 = 408 * 2 = 816 * 2 = 1664
for i in range(5):
    myResult = myResult * 2

print(myResult)

bank_account_balances = [5322.0, 577.35, -100.0]

for balance in bank_account_balances:
    print(balance)