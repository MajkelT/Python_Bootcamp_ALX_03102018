from django.http import HttpResponse
from django.shortcuts import render
from maths.models import Math

# Create your views here.

def obliczenia(request, obliczenia, a, b):
    a, b = int(a), int(b)  # rzutowanie
    print(a, b, obliczenia)
    # tu będą dodawane nowe rekordy ze strony www

    if obliczenia == "Add":
        return HttpResponse(a+b)
    if obliczenia == "Sub":
        return HttpResponse(a-b)
    if obliczenia == "Div":
        if b == 0:
            wynik = "Nie dziel przez zero cholero"
        else:
            wynik = a/b

    m = Math(operacja='Add', a=a, b=b, wynik=wynik)
    m.save()
    print(m.a, m.b, m.operacja)

    return HttpResponse(wynik)