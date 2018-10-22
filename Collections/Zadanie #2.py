i = 0
MojaLista = []

while i<10:   #albo len(MojaLista)<10

    x = input("Podaj wartość do listy: ")
    if x == "k":
        break
    MojaLista.append(int(x))
    i +=1
if len(MojaLista) == 0:
    print("Nie podano danych!")
else:
    print(MojaLista)
    b = sum(MojaLista) / len(MojaLista)
    print(b)

