from django.db import models

# Create your models here.
# klasa - dla aplikacji jest to jeden z modeli, ma budowe bazy danych
class Math(models.Model):
    operacja = models.CharField(max_length=4)    #liczba kolumn
    a = models.IntegerField()
    b = models.IntegerField()
    wynik = models.TextField()
    created = models.DateTimeField(auto_now=True)



#from math.models import Maths
#Math.objects.get(pk=1)  --> primary key
#Math.objects.filter(operacja='Add') --> pobiera tylko operacje, które są dodwawniem (Add)
#poczytaj o django querysets w dokumentacji - jakie zadawać zapytania do bazy danych
# ptyhon manage.py --> pokaże listę dostępnych funkcji

#TWORZENIE KONTA W PANELU ADMINISTRATORA:
#python manage.py createsuperuser   Majkel m@t.e kurs

#pip install django-suit i dodaj w examples --> settings.py INSTALLED_APPS = ['suit --> musi być pierwsze
