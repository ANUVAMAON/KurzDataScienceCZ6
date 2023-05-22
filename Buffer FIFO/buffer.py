class Sklad:

  def __init__(self, kapacita):
    self.kapacita = kapacita
    self.obsah = []

  def zobraz_obsah(self):
    print(self.obsah)

  def zaskladni(self, *args):
    for neco in args:
      if len(self.obsah) < self.kapacita:
        self.obsah.insert(0, neco)
      else:
        print("Nemůžu zaskladnit, sklad je plný")

  def vyskladni(self):
    if len(self.obsah) > 0:
      odebrano = self.obsah.pop()
      print(f"Odebral jsem {odebrano}")
    else:
      print("Nemám co vyskladnit!")

  def vyskladni_hromadne(self, kolik):
    if kolik > len(self.obsah):
      print("Tolik tam toho nemám, vyskladním vše!")
      tolik = len(self.obsah)
    else:
      tolik = kolik

    for i in range(tolik):
        odebrano = self.obsah.pop()
        print(f"Odebral jsem {odebrano}")