# żeby uruchomić serwer ptyhon manage.py runserver

from django.http import HttpResponse

def hello(request, imie=""):
    if not imie:
        imie = "World"
    return HttpResponse(f"Hello {imie}")



