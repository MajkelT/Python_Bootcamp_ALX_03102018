with open("dane/input.txt") as f:
    #print(dir(f))
    #print(f.read())
    # for linia in f:
    #     print(len(linia))

    for linia in f:
        if len(linia) > 600:
            print(linia)

f = open("dane/emails.txt")  #tak nie otwieramy plkiow
# musimy zamknac plik, bo inaczej plik bedzie caly czas w pamieci
f.close()

with open("info.txt", "w", encoding='utf8') as f:     #w - kasuje to co było wcześniej
    for i in range(10):
        f.write("Jaskis tekst\n")

with open("info.txt", "a", encoding='utf8') as f:    #a - append, r-jest domyślnie, wtedy nic nie trzeba
    f.write("Inny tekst")