import os
import django
import sys
import pandas as pd
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "expense_tracker_app.settings")
django.setup()

from home.models import Book, BookCategory
from format_excel import format_excel

file_to_format = "Books Distribution Expenses.xlsx"

# Leer el archivo Excel

def get_data_from_excel (filename):  
  data = pd.read_excel(filename)
  # Insertar los datos en la base de datos
  try:
    for _, row in data.iterrows():
        # Crear o buscar la categoría
        category, created = BookCategory.objects.get_or_create(name=row['category'])

        published_date = row['published_date']
        try:
          published_date = datetime.strptime(str(published_date), '%Y-%m-%d').date()
        except (ValueError, TypeError):
          published_date = None

        # Crear el libro
        book, created = Book.objects.update_or_create(
                isbn=row['id'],
                defaults={
                    'title': row['title'],
                    'subtitle': row['subtitle'],
                    'authors': row['authors'],
                    'publisher': row['publisher'],
                    'published_date': published_dategs,
                    'category': category,
                    'distribution_expense': row['distribution_expense']
                }
            )
  except Exception as e:
    raise Exception(f"Error al importar los datos de: {filename}, {e}")

formatted_file = format_excel(file_to_format) 

if __name__ == '__main__':
  get_data_from_excel(formatted_file)
  print(f"Archivo excel procesado y datos importados a la base de datos correctamente")