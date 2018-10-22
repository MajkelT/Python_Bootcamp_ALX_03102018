napis = input("Podaj napis: ")

samogłoski = 0

lista = ["a", "o", "i", "e", "u", "y", "ą", "ę"]  # może być też LISTA = "aeiouy"
for litera in napis.lower():
    if litera in lista:
            samogłoski += 1
print(f"W podanym napisie jest {samogłoski} samogłosek")