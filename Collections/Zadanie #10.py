napis = input("Podaj napis: ")

slownik = {}
for litera in napis.lower():

    if litera != " ":

    # if litera in slownik:
    #     slownik[litera] = slownik[litera] + 1
    # else:
    #     slownik[litera] = 1


        slownik[litera] = slownik.get(litera,0) + 1   #to wyrażenie zastępuje to co wyżej

print(slownik)



