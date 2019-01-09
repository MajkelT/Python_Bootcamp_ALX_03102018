from django.shortcuts import render
from books.models import Book
# Create your views here.


def book_list(request):   #wyświetli wszystkie książki, które mamy w bazie danych
    books = Book.objects.all()
    return render(
        template_name="books_list.html",
        context = {'books': books},
        request = request
    )