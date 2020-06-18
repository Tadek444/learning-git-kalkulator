#import logging
import sys
print ("Podaj dzialanie poslugując sie odpowiednim numerem:\n",
       "1.Dodawanie\n",
       "2.Odejmowanie\n",
       "3.Mnozenie\n",
       "4.Dzielenie")

def dzialanie(numer):
    if numer ==1:
        if skladniki ==2:
            dodawanie = float(pierwszy+drugi)
            print (f"Dodaję składniki:{pierwszy, drugi}") 
            print ("Wynik to:", dodawanie)
        elif skladniki ==3:
            dodawanie = float(pierwszy+drugi+trzeci)
            print (f"Dodaję składniki:{pierwszy, drugi, trzeci}") 
            print ("Wynik to:", dodawanie)

    elif numer == 2:
        odejmowanie = float(pierwszy-drugi)
        print (f"Odejmuję drugi składnik {drugi} od pierwszego {pierwszy}:")
        print ("Wynik to:", float(odejmowanie))

    elif numer == 3:
        if skladniki ==2:
            mnozenie = float(pierwszy*drugi)
            print (f"Mnożę składniki:{pierwszy, drugi}") 
        elif skladniki ==3:
            mnozenie = float(pierwszy*drugi*trzeci)
            print (f"Mnożę składniki:{pierwszy, drugi, trzeci}") 
        print ("Wynik to:", float(mnozenie))

    elif numer == 4:
        dzielenie = float(pierwszy/drugi)
        print (f"Dzielę pierwszy składnik: {pierwszy} przez drugi: {drugi}")    
        print ("Wynik to:", float(dzielenie))

    else:
        print ("numer działania spoza zakresu!!!")
        exit(1)
if __name__ == "__main__":
    numer = int(input("Podaj numer dzialania: "))
    if numer == 1:
        skladniki = int(input ("Podaj ilość składników:"))
        if skladniki == 2:
            pierwszy = float(input("Podaj pierwszy składnik: "))
            drugi = float(input("Podaj drugi składnik: "))
        elif skladniki == 3:
            pierwszy = float(input("Podaj pierwszy składnik: "))
            drugi = float(input("Podaj drugi składnik: "))
            trzeci = float(input("Podaj trzeci składnik: "))
        else:
            print ("Za dużo składników, proszę podać maksymalnie trzy!!!")
            exit (1)
    elif numer == 2:
        pierwszy = float(input("Podaj pierwszy składnik: "))
        drugi = float(input("Podaj drugi składnik: "))
    elif numer == 3:
        skladniki = int(input ("Podaj ilość składników:"))
        if skladniki == 2:
            pierwszy = float(input("Podaj pierwszy składnik: "))
            drugi = float(input("Podaj drugi składnik: "))
        elif skladniki == 3:
            pierwszy = float(input("Podaj pierwszy składnik: "))
            drugi = float(input("Podaj drugi składnik: "))
            trzeci = float(input("Podaj trzeci składnik: "))
        else:
            print ("Za dużo składników, proszę podać maksymalnie trzy!!!")
            exit (1)        
    elif numer == 4:
        pierwszy = float(input("Podaj pierwszy składnik: "))
        drugi = float(input("Podaj drugi składnik: "))
    dzialanie(numer)