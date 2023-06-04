import random
import os

def loteria():

    cisla_do_loterie = []


    while len(cisla_do_loterie) < 6:
        try:
            cislo = int(input("Zadajte cislo: "))
        except ValueError:
            print("Nezadal si cislo")
            continue
        if cislo in cisla_do_loterie:
            print("Toto cislo si uz zadal: ")
            continue
        if 49 >= cislo >= 1:
            print(f"Zadal jsi {cislo}")
            cisla_do_loterie.append(cislo)
        else:
            print("Zadane cislo je mimo rozsah 1 - 49!")

    return cisla_do_loterie


def losovanie():
    
    losovane_cisla = []

    while len(losovane_cisla) < 6:
        cislo = random.randint(1,49)
        if cislo in losovane_cisla:
            continue
        else:
            losovane_cisla.append(cislo)
    
    return losovane_cisla

def pokial_nevyhram(loteria):
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

    loteria.sort()
    los = losovanie()
    los.sort()

    pocet_losovani = 0
    print(f"\033[KTvoje cisla: {loteria}")
    while loteria != los:
        los = losovanie()
        los.sort()
        pocet_losovani += 1
        if pocet_losovani % 100000 == 0:
            
            print(f"\033[K{pocet_losovani}", los, end='\r')
    return pocet_losovani

stastne_cisla = loteria()
pocet_pokusov = int(pokial_nevyhram(stastne_cisla))
print(f"\033[K{stastne_cisla}")
print(f"Čakal by si na vyhru {pocet_pokusov / 6 / 52 } rokov a minul {pocet_pokusov* 1} €.")
