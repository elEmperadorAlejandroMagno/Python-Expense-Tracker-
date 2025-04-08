from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home, name="home"),
    path('index/', views.index, name="index"),
    path('books', views.get_books, name="books"),
    path('book/<int:id>', views.get_book_by_ID, name="book_by_ID"),
    path('get_categories', views.get_categories, name="get_book_categories"),
    path('get_distribution_expenses', views.get_distribution_expenses, name="get_distribution_expenses"),
  ]
