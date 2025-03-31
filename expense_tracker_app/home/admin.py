from django.contrib import admin
from .models import BookCategory, Book

# Registro del modelo de categorías
@admin.register(BookCategory)
class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Campos visibles en la lista de administración

# Registro del modelo de libros
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('isbn', 'title', 'subtitle', 'authors', 'publisher', 'published_date', 'category', 'distribution_expense')  # Campos visibles
    list_filter = ('category', 'published_date')  # Filtros para facilitar la búsqueda
    search_fields = ('title', 'authors')  # Campos para realizar búsquedas rápidas

