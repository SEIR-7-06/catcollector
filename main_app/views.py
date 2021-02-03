from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cat
from .forms import FeedingForm

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
  return render(request, 'cats/index.html', context)

def cats_detail(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
  # Creates a new instance of Feeding Form
  feeding_form = FeedingForm()

  context = {
    'cat': cat,
    'feeding_form': feeding_form
  }
  return render(request, 'cats/detail.html', context)

def add_feeding(request, cat_id):
  # Gets the data from the form
  form = FeedingForm(request.POST)

  # Checks if form data is valid
  if form.is_valid():
    # Converts form data into a usable format
    new_feeding = form.save(commit=False)
    # Adds the cat id to the new_feeding object
    new_feeding.cat_id = cat_id

    # Saves the New Feeding in the DB
    new_feeding.save()
  
  # - Redirects back to Cat Detail Page
  return redirect('cats_detail', cat_id=cat_id)