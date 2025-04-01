from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Book, BookCategory

# Create your views here.

def home(request):
  if request.method == 'GET':
    return HttpResponse("Hola, esta es la página principal de la app Home.")
  pass

def index(request):
  #view para renderizar los gráficos e información
  pass

def get_weekly(request):
  #renderizar los gastos semanales
  pass

def get_monthly(request):
  #renderizar los gastos mensuales
  pass

def get_annually(request):
  #renderizar los gastos anuales
  pass

def get_books(request):
  if request.method == 'GET':
    BOOKS = Book.objects.all()
    CATEGORIES = BookCategory.objects.all()
    return render(request, 'base_books.html', { 'books': BOOKS, 'categories': CATEGORIES })
  pass

def get_books_by_category(request):
  if request.method == 'GET':
    category = request.GET.get('category', None)
    if category:
      BOOKS = Book.objects.filter(category= filter) 
      return render(request, 'table_books.html', { 'books': BOOKS })
    else:
      BOOKS = Book.objects.all()
      messages.error("Categoría inválida")
      return redirect('books')
    

def get_book_by_ID(request, id):
  if request.method == 'GET':
    BOOK = get_object_or_404(Book, isbn=id)
    return render(request, 'book_details.html', {'book': BOOK})
  pass

def search(request):
  pass
