from django.db import models

class BookCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    isbn = models.CharField(max_length=13, unique=True, primary_key=True)  # ISBN como clave primaria
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    authors = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    published_date = models.DateField(blank=True, null=True)
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE, related_name='books')
    distribution_expense = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

