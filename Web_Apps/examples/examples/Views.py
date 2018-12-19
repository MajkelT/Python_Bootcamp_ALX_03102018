# żeby uruchomić serwer ptyhon manage.py runserver (musisz być w katalogu, w którym jest manage.py)
# python manage.py shell - uruchoamia shell (wcześniej pip install ipython - lepsza konsola)
# python manage.py showmigrations

from django.http import HttpResponse

def hello(request, imie=""):
    if not imie:
        imie = "World"
    return HttpResponse(f"Hello {imie}")



