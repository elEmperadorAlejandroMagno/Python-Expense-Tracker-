import sys
import os
import django
from django.db.models import Sum, Count

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "expense_tracker_app.settings")
django.setup()

from home.models import Book, BookCategory

def get_expenses_data(): 
  expenses = Book.objects.values('category__name').annotate(total_expense=Sum('distribution_expense'), books_quantity=Count('isbn'))
  expenses_data = [{'category': expense['category__name'], 'total_expenses': expense['total_expense'], 'books_quantity': expense['books_quantity']} for expense in expenses]
  return expenses_data

def get_categories_data():
  CATEGORIES = BookCategory.objects.all()
  CATEGORIES_DATA = [category.name for category in CATEGORIES]
  return CATEGORIES_DATA