def heslo():
    heslo = input("Zadajte vase heslo: ")
   
    while not kontrola_hesla(heslo):
        heslo = input("Zadajte vase heslo: ")

    return heslo

def kontrola_hesla(dakeheslo):
    dlzka_hesla = len(dakeheslo)
    velke_pismena = sum(map(str.isupper, dakeheslo))
    pocet_cisel = sum(p_c.isdigit() for p_c in dakeheslo)
    percento_cisel = int((pocet_cisel / len(dakeheslo)) * 100)

    if dlzka_hesla < 10:
        print("Heslo musi mat aspon 10 znakov!")
        
    elif velke_pismena < 2:
        print("Heslo musi mat aspon 2 velke pismena!")

    elif percento_cisel < 30:
        print(f"Heslo musi mat aspon 30% cisel")

    else:
        return True
    
            
subor = open("heslo.txt", "wt")
uloz_heslo = subor.write(heslo())
subor.close()