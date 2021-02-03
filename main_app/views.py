from django.shortcuts import render
from django.http import HttpResponse
from .models import Cat

# Create your views here.
def home(request):
  # return HttpResponse('<h1>Welcome to Cat Collector</h1>')
  return render(request, 'home.html')

def about(request):
  # return HttpResponse('<h1>All about the Cat Collector</h1>')
  return render(request, 'about.html')

def cats_index(request):
  cats = Cat.objects.all()
  context = { 'cats_data': cats }
  print(context)
  return render(request, 'cats/index.html', context)

def cats_detail(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
  context = { 'cat': cat }
  return render(request, 'cats/detail.html', context)
