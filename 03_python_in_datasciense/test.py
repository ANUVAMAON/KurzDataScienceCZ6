import os
import pickle

seznam = {}
for i in range(3):
  #první potřebuji od uživatele klíč -> např. iniciály
  inicialy = input("Zadej iniciály: ")
  #chci vyplnit vizitku
  vizitka = {}
  sloupce = ["jmeno", "prijmeni", "bydliste"]
  for sloupec in sloupce:
    vizitka[sloupec] = input(f"Zadej {sloupec}: ")
  #uložit do slovníku pod klíčem iniciály vizitku
  seznam[inicialy] = vizitka

def uloz_adresar(adresar, nazov_suboru):
    f = open(f'{nazov_suboru}.pkl', "wb")
    pickle.dump(adresar, f)
    f.close

def nacitaj_adresar(nazov_suboru):
    f = open(f'{nazov_suboru}.pkl', "rb")
    data = pickle.load(f)
    f.close()
    return data

uloz_adresar(seznam, "moj_zoznam")
skuska = nacitaj_adresar("moj_zoznam")

print(skuska)