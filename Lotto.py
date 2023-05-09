import random

amount = 6
maxNumber = 49
userNumbers = []
drawedNumbers = []
result = []

def drawNumbers(amount, maxNumber):
    return random.sample(range(1, maxNumber + 1), amount)

print("""1 - Chybił trafił
2 - Samodzielenie wybierz liczby""")

while (True):
    try:
        playMode = int(input("Wybierz tryb gry: "))
        if(playMode == 1 or playMode == 2):
            break
        else:
            print("Wybierz 1 lub 2")
            continue
    except ValueError:
        print("Podano nieprawidłową wartość")
        continue
    
if(playMode == 2):
    for i in range(amount):
        while (True):
            try:
                number = int(input(f"Podaj {i+1} Liczbę: "))
                if (number <= maxNumber and number > 0 and number not in userNumbers):
                    userNumbers.append(number)
                    break
                else:
                    print("Podano liczbę spoza zakresu lub liczba została już dodana")
                    continue
            except ValueError:
                print("Podaj LICZBĘ")
                continue
else:
    userNumbers = drawNumbers(amount, maxNumber)
drawedNumbers = drawNumbers(amount, maxNumber)
    
print("Twoje liczby:     ", userNumbers)
print("Wylosowane liczby:", drawedNumbers)
result = (set(userNumbers) & set(drawedNumbers))
if((len(result) > 0)):
    print("Gratulacje! Trafiono liczby:", result)
else:
    print("Nie trafiono żadnej liczby...")
