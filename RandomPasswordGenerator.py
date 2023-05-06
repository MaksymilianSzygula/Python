import string
import random

lowerCase = string.ascii_lowercase
upperCase = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation
string = ""
password = ""

print("GENERATOR LOSOWYCH HASEŁ")

while (True):
    try:
        passwordLength = abs(int(input("Podaj długość hasła: ")))
    except ValueError:
        print("Podaj odpowiednią wartość liczbową")
        continue
    else:
        break

print("Wybór znaków [t - TAK / Dowolny inny znak - NIE")
useLowerCase = input("Małe litery: ")
if(useLowerCase.lower() == "t"):
    string += lowerCase
useUpperCase = input("Duże litery: ")
if(useUpperCase.lower() == "t"):
    string += upperCase
useDigits = input("Cyfry: ")
if(useDigits.lower() == "t"):
    string += digits
useSymbols = input("Znaki specjalne: ")
if(useSymbols.lower() == "t"):
    string += symbols

if(len(string) > 0):
    password = "".join(random.choice(string) for i in range(passwordLength))
    print("Twoje hasło to:", password)
else:
    print("Nie wybrano żadnych znaków do utworzenia hasła!")
