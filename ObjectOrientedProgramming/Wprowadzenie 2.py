class Osoba():
    imie = "Jan"
    nazwisko = "Kowalski"
                                        # self - to instantja obiektu, na którym coś jest wywoływane
                                        # musi być użyte dla każdej metody niestatycznej
    def __init__(self, imie, nazwisko):  #metoda specjalna - oznaczona i zakończona podkreślnikami
        print("No siema")
    #zdefiniowanie metydy przedstaw_sie:
    def przedstaw_sie(self):
        print(f"Nazywam się {self.imie} {self.nazwisko}")

    @staticmethod
    def metoda_statyczna():
        print("Metoda statyczna")

#obiekt = Osoba()  #tworzymy nowy obiekt klasy osoba - musi mieć nawiasy
#obiekt2 = Osoba()
#obiekt2.imie = "Karol"

#instancja klasy osoba = zmienna typu osoba

obiekt = Osoba("Adam", "Małysz")
obiekt2 = Osoba("Michał", "Tuczyński")
obiekt.przedstaw_sie()
obiekt2.przedstaw_sie()
Osoba.metoda_statyczna()
