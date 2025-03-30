from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def home(request):
  if request.method == 'GET':
    return HttpResponse("Hola, esta es la página principal de la app Home.")
  pass

def index(request):
  pass

def get_weekly(request):
  pass

def get_monthly(request):
  pass

def get_annually(request):
  pass

def get_books(request):
  pass

def get_book_by_ID(request):
  pass

def get_categories(request):
  pass

def search(request):
  pass
