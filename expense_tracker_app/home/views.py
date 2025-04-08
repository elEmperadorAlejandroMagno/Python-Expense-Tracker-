# from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.db import models
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
    
    # Chart data
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
      return JsonResponse(expenses_list, safe=False)

    return render(request, 'index.html', { 'data': expenses_list, 'groupedBy': multiplier_key })
  pass
  
def get_books(request):
  if request.method == 'GET':
    search_query = request.GET.get('search', '')
    category_query = request.GET.get('category', None)

    if search_query:
      BOOKS = Book.objects.filter(
          models.Q(title__icontains=search_query) |
          models.Q(isbn__icontains=search_query)
      )
    elif category_query:
      if category_query == 'All':
        BOOKS = Book.objects.all()
      else:
        CATEGORY = BookCategory.objects.get(name=category_query)
        BOOKS = Book.objects.filter(category=CATEGORY)
    else:
      BOOKS = Book.objects.all()
    CATEGORIES = get_categories_data()
    return render(request, 'table_books.html', { 'books': BOOKS, 'categories': CATEGORIES, 'filter': category_query })
  pass

def get_book_by_ID(request, id):
  if request.method == 'GET':
    BOOK = get_object_or_404(Book, isbn=id)
    return render(request, 'book_details.html', {'book': BOOK})
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