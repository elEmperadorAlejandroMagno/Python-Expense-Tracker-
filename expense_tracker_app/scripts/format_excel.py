import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_DIR = os.path.join(BASE_DIR, 'files')

def format_excel(filename):
  filename = os.path.join(FILE_DIR, filename)
  try:
    data = pd.read_excel(filename)

    duplicados = data[data.duplicated()]
    if not duplicados.empty:
      print("Datos duplicados encontrados:")
      print(duplicados)
      data = data.drop_duplicates()

    data["category"] = data["category"].fillna("Other")

    data["category"] = data["category"].str.title()

    formatted_filename = f"{filename}_formatted.xlsx"

    data.to_excel(formatted_filename, index=False)
    return formatted_filename
  except Exception as e:
    raise Exception(f"Error al procesar y formatear el archivo {filename}")
  
if __name__ == '__main__':

  test_filename = os.path.join(FILE_DIR, "Books Distribution Expenses.xlsx")

  try:
    data = pd.read_excel(test_filename)
    duplicados = data[data.duplicated()]

    if not duplicados.empty:
      print("Datos Duplicados:")
      print(duplicados)

    formatted_file = format_excel(test_filename)
    print(f"archivo formateado guardado en: {formatted_file}")
  except Exception as e:
    print(f"Error durante las pruebas: {e}")