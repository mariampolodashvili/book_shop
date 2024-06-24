from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.
def home(request):
    books = Book.objects.all()
    context={"books":books}
    return render(request, 'home.html', context)

