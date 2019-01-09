from django.contrib import admin
from .models import Math

# Register your models here.

class AdminMath(admin.ModelAdmin):     #ta klasa
    list_display = ['operacja', 'a' ,'b', 'wynik', 'created']   #kolumny
    list_filter = ['operacja']    #filtry na stronie
    search_fields = ['wynik']       #pole szukania



admin.site.register(Math, AdminMath)      #zarejestrowałem moduł math w panelu administratora
#zarządzaniem obiektem Math będzie sie zajmował AdminMath
