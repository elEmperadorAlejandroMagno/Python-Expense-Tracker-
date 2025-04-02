# from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from .models import Book
from scripts.help import get_expenses_data, get_categories_data

# Create your views here.

def home(request):
  if request.method == 'GET':
    return render(request, 'base.html')
  pass

def index(request):
  if request.method == 'GET':
    expenses_list = get_expenses_data()
    return render(request, 'index.html', { 'data': expenses_list})
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
    CATEGORIES = get_categories_data()
    return render(request, 'table_books.html', { 'books': BOOKS, 'categories': CATEGORIES })
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

def get_categories(request):
    if request.method == 'GET':
      categories_list = get_categories_data()
      return JsonResponse(categories_list, safe=False)
    pass

def get_distribution_expenses(request):
  if request.method == 'GET':
    expenses_data = get_expenses_data()
    return JsonResponse(expenses_data, safe=False)
  pass