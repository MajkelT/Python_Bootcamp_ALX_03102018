# list = [1,2,4,5,6,7,8,9,10,-11,-12,-13,-14,-15,0]
# liczbyDodatnie = []
# liczbyUjemne = []
# for liczba in list:
#     if liczba >0:
#         liczbyDodatnie.append(liczba)
#     elif liczba <0:
#         liczbyUjemne.append(liczba)
#
# print(liczbyDodatnie)
# print(liczbyUjemne)
# print(f"Ilość liczb dodatnich to: {len(liczbyDodatnie)}")
# print(f"Ilość liczb dodatnich to: {len(liczbyUjemne)}")

list = [1,2,4,5,6,7,8,9,10,-11,-12,-13,-14,-15,0]
liczbyDodatnie = 0
liczbyUjemne = 0
for liczba in list:
    if liczba >0:
        liczbyDodatnie += 1
    elif liczba <0:
        liczbyUjemne += 1
print(liczbyDodatnie)
print(liczbyUjemne)