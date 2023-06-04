import pickle
import json

class kontakt:
  def __init__(self, meno, priezvisko, firma):
    self.meno = meno
    self.priezvisko = priezvisko
    self.firma = firma

  def vytlac(self):
    print("Meno: ", self.meno)
    print("Priezvisko: ", self.priezvisko)
    print("Firma: ", self.firma)

  def slovnik(self):
    slovnik = {}
    slovnik["meno"] = self.meno
    slovnik["priezvisko"] = self.priezvisko
    slovnik["firma"] = self.firma
    return slovnik


id_1 = kontakt("Michal", "Maliszewski", "Barclays")
id_2 = kontakt("Milos", "Zeman", "Duchod")
id_3 = kontakt("Petr", "Fiala", "Premier")


class Adresar:
  def __init__(self, nazov):
    self.plna_cesta = nazov + ".pkl"
    self.data = {}
    self.id= 0

  def zobraz_adresar(self):
    print(self.data)

  def uloz_adresar(self):
    with open(self.plna_cesta, "w") as file:
      json.dump(self.data, file)
  
  def nacitaj_adresar(self):
    with open(self.plna_cesta, "r") as file:
      json.load(self.data, file)
  
  def pridaj_kontakt(self, kontakt):
    self.data[self.id] = kontakt
    self.id =+ 1
    pass
  
  def vyhladaj_kontakt(self, priezvisko):
    pass
  
  def zmaz_vybrany(self, kontakt):
    pass
  
  def zmaz_vsetko(self):
    self.data = {}

adr = Adresar
adr.uloz_adresar()