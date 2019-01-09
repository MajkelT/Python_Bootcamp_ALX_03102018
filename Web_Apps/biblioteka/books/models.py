from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)       #ramka na tekst z ograniczona liczba znakow
    author = models.CharField(max_length=200)
    decription = models.TextField()     #pole tekstowe y nieograniczoną liczbą znaków
    cover = models.ImageField(upload_to="books_covers/%Y/%m/%d")  #rok/miesiąc/dzień

    def __str__(self):
        return f'{self.title} - {self.author}'


