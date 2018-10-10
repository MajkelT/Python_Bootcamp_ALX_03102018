x = int(input("podaj X:"))
y = int(input("podaj Y:"))
poz = (x,y)
if x<=10 and y<=10:
    print("LD", poz)
elif x>=90 and x<=100 and y<=10:
    print("PD", poz)
elif x>10 and x<90 and y<=10 and y>0:
    print("DK", poz)
elif x<=10 and x>=0 and y>=90 and y<=100:
    print("LG" ,poz)
elif x<=10 and x>=0 and y>10 and y<90:
    print("LK", poz)
elif x>=90 and x<=100 and y>10 and y<90:
    print("PK", poz)
elif x>10 and x<90 and y>=90 and y<=100:
    print("GK", poz)
elif x>=90 and x<=100 and y>=90 and y<=100:
    print("PG", poz)
elif x>10 and x<90 and y>10 and y<90:
    print("CENTRUM", poz)
else:
    print("Gdzieś masz błąd, X musi być <= 100 i Y musi być <=100")

