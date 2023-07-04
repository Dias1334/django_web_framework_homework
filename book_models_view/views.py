from django.shortcuts import render

from book_models_view.models import Books


# Create your views here.

def book_view(request):
    books_view = Books.objects.all()
    return render(request, 'index.html', {'books_view': books_view})
