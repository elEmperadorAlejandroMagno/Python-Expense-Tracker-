import os
import django
import sys
import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "expense_tracker_app.settings")
django.setup()

from home.models import Book, BookCategory
from format_excel import format_excel

file_to_format = "Books Distribution Expenses"

# Leer el archivo Excel

def get_data_from_excel (filename):  
  data = pd.read_excel(filename)
  # Insertar los datos en la base de datos
  try:
    for _, row in data.iterrows():
        # Crear o buscar la categoría
        category, created = BookCategory.objects.get_or_create(name=row['category'])

        # Crear el libro
        Book.objects.create(
            isbn=row['id'],
            title=row['title'],
            subtitle=row['subtitle'],
            authors=row['authors'],
            publisher=row['publisher'],
            published_date=row['published_date'],
            category=category,
            distribution_expense=row['distribution_expense']
        )
  except Exception as e:
    raise Exception(f"Error al procesar el archivo {filename}: {e}")

filename = format_excel(file_to_format) 

if __name__ == '__main__':
  get_data_from_excel(filename)