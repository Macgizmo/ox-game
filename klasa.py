#class mojaklasa:
#   def wyświetl ():
#      return 'Witaj świecie'

#x=mojaklasa()
# print(x.wyświetl())

class prostopadloscian:
    def _init_(self):
        self.podstawa_a=0
        self.podstawa_b=0
        self.wysokość_h=0
    def objetosc (self):
        return self.podstawa_a*self.podstawa_b*self.wysokość_h
#%
wtc= prostopadloscian()
wtc.podstawa_a=100
wtc.podstawa_b=200
wtc.wysokość_h=100
print(wtc.objentosc())