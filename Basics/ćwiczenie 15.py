from random import randint

skarbX = randint(1, 10)
skarbY = randint(1, 10)
graczX = randint(1, 10)
graczY = randint(1, 10)
print("X gracz: ", graczX, "Y gracz: ", graczY)
#print("X skarb: ", skarbX, "Y skarb: ", skarbY)
#print(f"Od skarbu dzieli cię: {abs(skarbX-graczX)}, {abs(skarbY-graczY)}")
minKrokowPrzed = abs(skarbX - graczX) + abs(skarbY - graczY)
print("Jak chcesz zakończyć grę, wpisz \"koniec\"")
i = 0

while True:
    if graczX == skarbX and graczY == skarbY:  # lub if minKrokowPo == 0:
        print ("Znalazłeś skarb")
        print ("Liczba ruchów do ukończenia gry, to: ", i)
        break
    if graczX > 10 or graczY > 10 or graczX < 0 or graczY < 0:
        print ("Jesteś poza planszą, koniec gry!")
        break
    else: ruch = input("Podaj kierunek ruchu (wsad) lub wpisz \"koniec\": ")

    if ruch == "koniec":
        print("Jesteś dupa")
        break
    if ruch == "w":
        graczY+= 1
    if ruch == "s":
        graczY-= 1
    if ruch == "a":
        graczX-= 1
    if ruch == "d":
        graczX+= 1
    print("X gracz: ", graczX, "Y gracz: ", graczY)
    #print("X skarb: ", skarbX, "Y skarb: ", skarbY)
    #print(f"Od skarbu dzieli cię: {abs(skarbX-graczX)}, {abs(skarbY-graczY)}")

    minKrokowPo = abs(skarbX - graczX) + abs(skarbY - graczY)
    if randint(1, 5)<5:
        if minKrokowPrzed < minKrokowPo:
            print("Oddalasz się")
            print(f"Jesteś {minKrokowPo} kroków od skarbu")
        else:
            print("Zbliżasz się")
            print(f"Jesteś {minKrokowPo} kroków od skarbu")
    else:
        print("Masz pecha, tym razem nie będzie wskazówki")

    i+= 1
