import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_DIR = os.path.join(BASE_DIR, 'files')

# def validate_date(date):
#   try:
#     return datetime.strptime(str(date), '%Y-%m-%d').date()
#   except (ValueError, TypeError):
#     return None

def format_excel(filename):
  filepath = os.path.join(FILE_DIR, filename)
  try:
    data = pd.read_excel(filepath)

    duplicados = data[data.duplicated(subset=['id'])]

    if not duplicados.empty:
      print("Datos duplicados encontrados:")
      print(duplicados)

    data = data.drop_duplicates(subset=['id'])

    data["category"] = data["category"].fillna("Other")

    data["category"] = data["category"].str.title()

    formatted_filename = filepath[:-5] + '_formatted' + filepath[-5:]
    data.to_excel(formatted_filename, index=False)

    print(f"Archivo formateado guardado en: {formatted_filename}")
    return formatted_filename
  except Exception as e:
    raise Exception(f"Error al procesar y formatear el archivo: {filename}")
  
if __name__ == '__main__':
  formatted_file = format_excel("Books Distribution Expenses.xlsx")