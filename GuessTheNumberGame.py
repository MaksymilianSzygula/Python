import random

guessNumber = 0
guessCount = 0
numberMin = 0
numberMax = 0

def inputNumber():
  while (True):
      print("Podaj zakres liczb ")
      global numberMin, numberMax
      try:
          numberMin = abs(int(input("Liczba od: ")))
          numberMax = abs(int(input("Liczba do: ")))
          if(numberMax < numberMin):
              print("Podano błędną wartość: MAX < MIN")
              continue
          else:
              break
      except ValueError:
          print("Podaj LICZBĘ!")
          
inputNumber()
correctNumber = random.randint(numberMin, numberMax)

while(guessNumber != correctNumber):
    guessCount += 1
    try:
        guessNumber = int(input("Odgadnij Liczbę: "))
    except ValueError:
        print("Podaj LICZBĘ!")
        continue
    if(guessNumber > correctNumber):
        print("Podałeś za dużą liczbę")
    elif(guessNumber < correctNumber):
        print("Podałeś za małą liczbę")
    else:
        print("Brawo! Szukana liczba to:", correctNumber)
        print("Liczba prób:", guessCount)
