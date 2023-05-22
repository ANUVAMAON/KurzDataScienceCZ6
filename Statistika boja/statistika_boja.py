from random import randint

class Postava:

  def __init__(self, jmeno, zivoty=100, utok_min=5, utok_max=10, stit=2):
    self.jmeno = jmeno
    self.zivoty = zivoty
    self.zije = True
    self.utok_min = utok_min
    self.utok_max = utok_max
    self.stit = stit

  def ukaz_zivoty(self):
    print(f"{self.jmeno} má životů {self.zivoty}")

  def utok(self):
    return randint(self.utok_min, self.utok_max)

  def obrana(self, rana):
    if rana > self.stit:
      self.zivoty = self.zivoty - rana + self.stit
    if self.zivoty < 1:
      print(f"Dostal jsi mě, {self.jmeno} je mrtev!")
      self.zije = False

michal = Postava("Michal", 1000, utok_min=0, utok_max=2, stit=10)
niki = Postava("Nikola", 100, utok_min=50, utok_max=100, stit=1)

def mortal_combat(bojovnik_dobro, bojovnik_zlo):
  bojovnici = [bojovnik_dobro, bojovnik_zlo]
  max_rana = 0
  while bojovnici[0].zije and bojovnici[1].zije:
    los = bool(randint(0, 1))
    rana = bojovnici[int(not los)].utok()
    bojovnici[int(los)].obrana(rana)

    if rana > max_rana:
      max_rana = rana

  if bojovnici[0].zije:
    jmeno = bojovnici[0].jmeno
    zivoty = bojovnici[0].zivoty
  else:
    jmeno = bojovnici[1].jmeno
    zivoty = bojovnici[1].zivoty
    
  return jmeno, zivoty, max_rana


vysledky = []
michal_vyhra = 0
michal_zivoty = []
niki_vyhra = 0
niki_zivoty = []

pocet_her = 10000
m_zivoty = 1000
n_zivoty = 130

for i in range(pocet_her):
  michal = Postava("Michal", m_zivoty, utok_min=5, utok_max=10, stit=10)
  niki = Postava("Nikola", n_zivoty, utok_min=20, utok_max=100, stit=1)
  vitez, zivoty, max_rana = mortal_combat(michal, niki)
  if vitez == "Michal":
    michal_vyhra += 1
    michal_zivoty.append(zivoty)
  else:
    niki_vyhra += 1
    niki_zivoty.append(zivoty)

