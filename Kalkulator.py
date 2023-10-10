from enum import IntEnum

aText = ""
bText = ""

def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    return a / b

def potegowanie(a, b):
    return a ** b

def pierwiastkowanie(a, b):
    return round(a ** (1 / b), 3) # Round to 3 Decimal Places

def modulo(a, b):
    return a % b

def inputStringText():
    global aText, bText
    if(wybor in range(1,4 + 1) or wybor == Menu.Modulo):
        aText = "Podaj A: "
        bText = "Podaj B: "
    elif(wybor == Menu.Potegowanie):
        aText = "Liczba: "
        bText = "Potęga: "
    elif(wybor == Menu.Pierwiastkowanie):
        aText = "Liczba: "
        bText = "Stopień pierwiastka: "

print("""Kalkulator - wybierz jedną z dostępnych opcji:
1 - Mnożenie
2 - Dzielenie
3 - Dodawanie
4 - Odejmownaie
5 - Potęgowanie
6 - Pierwiastkowanie
7 - Reszta z dzielenia (Modulo)""")

Menu = IntEnum("Menu","Mnozenie Dzielenie Dodawanie Odejmowanie Potegowanie Pierwiastkowanie Modulo")

while True:
    while True:
        try:
            wybor = int(input("Wybierz działanie: "))
            if(wybor in range(1, len(Menu) + 1)):
                inputStringText()
                a = int(input(aText))
                b = int(input(bText))
                break
            else:
                print("Wybierz jedną z dostępnych opcji (1 - 7)")
        except ValueError:
            print("Podano błędną wartość")

    if (wybor == Menu.Mnozenie):
        print(f"{a} * {b} = {mnozenie(a, b)}")
    elif (wybor == Menu.Dzielenie):
        try:
            print(f"{a} / {b} = {dzielenie(a, b)}")
        except ZeroDivisionError:
            print("Dzielenie przez 0!")
    elif (wybor == Menu.Dodawanie):
        print(f"{a} + {b} = {dodawanie(a, b)}")
    elif (wybor == Menu.Odejmowanie):
        print(f"{a} - {b} = {odejmowanie(a, b)}")
    elif (wybor == Menu.Potegowanie):
        print(f"{a} ** {b} = {potegowanie(a, b)}")
    elif (wybor == Menu.Pierwiastkowanie):
        print(f"Pierwiastek {b}-stopnia z {a} = {pierwiastkowanie(a, b)}")
    elif (wybor == Menu.Modulo):
        print(f"{a} % {b} = {modulo(a, b)}")
