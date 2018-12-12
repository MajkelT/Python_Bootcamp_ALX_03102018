import tkinter


def jakas_funkcja():
    wartosc1 = float(entry1.get())
    wartosc2 = int(entry2.get())
    wartosc3 = entry3.get()
    wartosc4 = round(wartosc1*wartosc2,3)
    label4.configure(text=wartosc4)  # wpisanie tekstu do okna podmieni label
    #print(f"Cena za przejazd samochodem: {wartosc3} wynosi {wartosc1*wartosc2} złotych.")

root = tkinter.Tk()  # obiekt klasy Tk przypisany do zmiennej root
root.columnconfigure(1)

entry1 = tkinter.Entry(master=root)  # pole tekstowe
entry1.grid(row=0, column=0)  # pole tekstowe ma byc w wierszu 1 i kolumnie 1 (python liczy od 0) - cena paliwa
label = tkinter.Label(master=root, text="Cena paliwa za litr w PLN")  # label, etykietka, napis ->
label.grid(row=0, column=1)

entry2 = tkinter.Entry(master=root)
entry2.grid(row=1, column=0)  # odlegołość przejechana
label = tkinter.Label(master=root, text="Ilość przejechanych kilometrów")  # label, etykietka, napis ->
label.grid(row=1, column=1)

entry3 = tkinter.Entry(master=root)
entry3.grid(row=2, column=0)   # ilość kilometrów
label = tkinter.Label(master=root, text="Marka samochodu")  # label, etykietka, napis ->
label.grid(row=2, column=1)

button = tkinter.Button(master=root, text="Oblicz koszt przejazdu!", command=jakas_funkcja)
button.grid(row=3, column=0)
label4 = tkinter.Label(master=root, text="")  # label, etykietka, napis ->
label4.grid(row=3, column=1)


root.mainloop()  # odpalam metodé mainloop na tym root'cie
