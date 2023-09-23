myAge = 26

myResult = myAge * 2

# <, >, <=, >=, ==, !=

# prüft von oben nach unten alle Bedingungen und die dann zutrifft, wird ausgeführt 
if myAge > 18:
    print("You are an adult!")
elif myAge == 18: 
    print("Congrats you are now an adult!")
else:
    print("You are not an adult!")

for i in range(5):
    myResult = myResult * 2

print(myResult)
