# from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from .models import Book, BookCategory
from scripts.help import get_expenses_data, get_categories_data

# Create your views here.

def home(request):
  if request.method == 'GET':
    return render(request, 'base.html')
  pass

def index(request):
  if request.method == 'GET':
    multiplier_map = {
        'day': 1,
        'week': 7,
        'month': 30,
        'year': 365
    }

    multiplier_key = request.GET.get('groupedBy')
    multiplier = multiplier_map.get(multiplier_key, 1)

    expenses_list = get_expenses_data()
    for item in expenses_list:
      item['total_expenses'] = round(item['total_expenses'] * multiplier, 2)

    return render(request, 'index.html', { 'data': expenses_list, 'groupedBy': multiplier_key })
  pass

# def get_expenses_with_multiplier(request):
  
def get_books(request):
  if request.method == 'GET':
    BOOKS = Book.objects.all()
    CATEGORIES = get_categories_data()
    return render(request, 'table_books.html', { 'books': BOOKS, 'categories': CATEGORIES })
  pass

def get_books_by_category(request):
    if request.method == 'GET':
        category_name = request.GET.get('category', None)
        if category_name:
            try:
                # Buscar la categoría por nombre
                category = BookCategory.objects.get(name__iexact=category_name)  # Insensible a mayúsculas/minúsculas
                print(category)
                # Filtrar libros por la categoría encontrada
                BOOKS = Book.objects.filter(category=category)
                CATEGORIES = get_categories_data()
                return render(request, 'table_books.html', {'books': BOOKS, 'filter': category, 'categories': CATEGORIES })
            except BookCategory.DoesNotExist:
                messages.error(request, f"No se encontró la categoría '{category_name}'.")
                return redirect('books')
            except Exception as e:
                messages.error(request, f"Error al filtrar libros: {e}")
                return redirect('books')
        else:
            messages.error(request, "Categoría inválida o no proporcionada.")
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