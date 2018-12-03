from random import randint
from Zadanie4aPrzedmiot import Przedmiot

class Postac():
    def __init__(self, imie, atak, zdrowie):
        self.imie = imie
        self._atak = atak
        self.zdrowie = zdrowie
    # zdrowie trzeba rozbić dodatkowo, bo będzie zmienne
        self.max_zdrowie = zdrowie
        self.ekwipunek = []    #tu będą przedmioty dające extra atak, tego nie definiujesz przy tworzeniu psotaci
                               #stąd nie ma tego za __init__(...)
    @property         #dynamiczny atrybut
    def atak(self):
        atak_xtra = self._atak
        for przedmiot in self.ekwipunek:
            atak_xtra += przedmiot.bonus_atk
        return atak_xtra


    #stwórzmy metodę, że nasza postać potrafi się przedstawić:
    def przedstaw_sie(self):
        print(f"Jestem {self.imie}, mam {self.atak} ataku i {self.zdrowie}/{self.max_zdrowie} życia.")

    def __str__(self):    #__init__ służy do tworzenia, a ta metoda przerabia dany obiekt na napis
        if self.czy_zyje() == True:
            napis = "EKWIPUNEK:\n"
            for x in self.ekwipunek:
                napis += str(x) + "\n"
            return(f"Jestem {self.imie}, mam {self.atak} ataku i {self.zdrowie}/{self.max_zdrowie} życia.\n") + napis
        else:
            return(f"Cześć byłem {self.imie}, ale już mnie nie ma")
    #teraz Print(rufus) da nam ten napis zdefiniowany jako __str__

    #chcemy, żeby postać mogła oberwac i robimy metodę otrzymaj obrażenia:
    def otrzymane_obrazenia(self, ile):
        #print (f"{self.imie} oberwał za {ile} obrażeń.")   #to jest opisane w walce
        self.zdrowie -= ile
        if self.zdrowie <= 0:
            self.zdrowie = 0

    def czy_zyje(self):
        # if self.zdrowie <= 0:
        #     return False   #do zwracania służy return, a nie czy_zyje = False!
        # return True     #nie trzeba else, po return wychodzi z funkcji

        # krótsza droga to:
        return self.zdrowie > 0   #siłą rzeczy zwróci True lub False

    def wylecz(self, healing):
        if self.czy_zyje() == True:
            if (self.zdrowie + healing) > self.max_zdrowie:
                self.zdrowie = self.max_zdrowie
            else:
                self.zdrowie += healing
        else:
            return print("Jeseś martwy, nie możesz się leczyć!")

    def respawn(self):
        pass

    def moc_ataku(self):
        return randint(self.atak//2, int(self.atak*1.5))    #//2 - zwróci liczbę całkowitą

    def daj_przedmiot(self,przedmiot):
        self.ekwipunek.append(przedmiot)

    # def atak_pus(self):  # dodatkowy atak z sily przedmiotu
    #     atak_xtra = self.atak
    #     for przedmiot in self.ekwipunek:
    #         atak_xtra += przedmiot.bonus_atk
    #     return atak_xtra

    #taki dekorator musi być do definiowania zmiennej statycznej
    @staticmethod
    def walka(atakujacy, broniacy):
        print(f"Walka: {atakujacy.imie} vs {broniacy.imie}")

        while atakujacy.czy_zyje() and broniacy.czy_zyje():
            print(atakujacy)
            print(broniacy)
            atak_atakujacego = atakujacy.moc_ataku()
            atak_broniacego = broniacy.moc_ataku()
            print(f"{atakujacy.imie} uderza {broniacy.imie} za {atak_atakujacego} obrażeń")
            broniacy.otrzymane_obrazenia(atak_atakujacego)
            print(f"{broniacy.imie} uderza {atakujacy.imie} za {atak_broniacego} obrażeń")
            atakujacy.otrzymane_obrazenia(atak_broniacego)
        print("KONIEC WALKI")

# rufus = Postac("Rufus", 3, 100)
# rufus.przedstaw_sie()
# print(rufus)
# rufus.otrzymane_obrazenia(30)
# print(rufus)
# rufus.otrzymane_obrazenia(100)
# print(rufus)
# rufus.wylecz(20)

#walka:
rufus = Postac("Rufus", 65, 800)
janusz = Postac("Janusz", 70, 800)
#tworzymy przedmioty:
tulipan = Przedmiot("Zielony tulipan zniszczenia", 5)
rufus.daj_przedmiot(tulipan)
#print(f"bonus atak: {rufus.atak_pus()}")

Postac.walka(rufus, janusz)
print(rufus)
print(janusz)




def test_nowa_postac():
    postac = Postac("Albert", 1, 20)
    assert postac.imie == "Albert" and postac.atak == 1 and postac.zdrowie == 20 and postac.max_zdrowie == 20

def test_obrazenia():
    postac = Postac("Rafał", 5, 200)
    assert postac.zdrowie == 200
    postac.otrzymane_obrazenia(80)
    assert postac.zdrowie == 120
    postac.otrzymane_obrazenia(200)
    assert postac.zdrowie == 0

def test_leczenie_nieboszczyka():
    postac = Postac("Rafał", 5, 200)
    postac.otrzymane_obrazenia(800)
    assert postac.zdrowie == 0
    postac.wylecz(50)
    assert postac.zdrowie == 0

def test_za_duze_leczenie():
    postac = Postac("Rafał", 5, 200)
    postac.otrzymane_obrazenia(80)
    assert postac.zdrowie == 120
    postac.wylecz(500)
    assert postac.zdrowie == 200
