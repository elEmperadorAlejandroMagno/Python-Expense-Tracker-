from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home, name="home"),
    path('index/', views.index, name="index"),
    # path('get_expenses_with_multiplier', views.get_expenses_with_multiplier, name="multiply_expenses"),

    path('books', views.get_books, name="books"),
    path('books/', views.get_books_by_category, name="books_filtered"),
    path('book/<int:id>', views.get_book_by_ID, name="book_by_ID"),
    path('search', views.search, name="search"),

    path('get_categories', views.get_categories, name="get_book_categories"),
    path('get_distribution_expenses', views.get_distribution_expenses, name="get_distribution_expenses"),
    
    
    #auth paths
    # path('/singup', views.singup, name="handleSingup"),
    # path('/login', views.login, name="handleLogin"),
    # path('/logout', views.logout, name="handleLogoun"),
    # path('/reset_password', views.reset_password, name="handleResetPassword"),
    # path('/reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name='reset_password_sent.html'), name="resetPasswordSent"),
    # path('/reset/<uidb64>/<token>', views.reset_password_confirm, name="resetPasswordConfirm"),
    # path('/reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name='reset_password_complete.html'), name="resetPasswordComplete")
  ]
