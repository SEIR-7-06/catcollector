from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cat, Toy
from .forms import FeedingForm, CatForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
  return render(request, 'home.html')






def about(request):
  return render(request, 'about.html')





@login_required
def cats_index(request):
  # If Post request Add a new cat to the DB
  if request.method == 'POST':
    cat_form = CatForm(request.POST)

    if cat_form.is_valid():
      new_cat = cat_form.save(commit=False)
      new_cat.user_id = request.user.id
      new_cat.save()

  cats = Cat.objects.filter(user=request.user)
  cat_form = CatForm()
  context = {
    'cats_data': cats,
    'cat_form': cat_form
  }
  return render(request, 'cats/index.html', context)





@login_required
def cats_detail(request, cat_id):
  # cat = Cat.objects.get(id=cat_id)
  cat = Cat.objects.filter(id=cat_id)
  # Creates a new instance of Feeding Form
  feeding_form = FeedingForm()

  # Query toys cat does not have
  toys_cat_doesnt_have = Toy.objects.exclude(id__in=cat.toys.all().values_list('id'))

  context = {
    'cat': cat,
    'feeding_form': feeding_form,
    'toys': toys_cat_doesnt_have
  }
  return render(request, 'cats/detail.html', context)




@login_required
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





@login_required
def assoc_toy(request, cat_id, toy_id):
  cat = Cat.objects.get(id=cat_id)
  cat.toys.add(toy_id)

  return redirect('cats_detail', cat_id=cat_id)





##################################################
# LOGIN ROUTES
##################################################
def signup(request):
  error_message = ''

  # IF POST REQUEST SUBMIT SIGNUP FORM
  if request.method == 'POST':
    # Get the data from the request body
    form = UserCreationForm(request.POST)

    # If data is valid
    if form.is_valid():
      # Save new user in DB
      user = form.save()
      # Tell Django to login our user
      login(request, user)
      # Take them to the cats index page
      return redirect('cats_index')

    else:
      error_message = 'Invalid singup credentials - Try again.'


  print('*** Hit the signup view!')
  # IF GET REQUEST SHOW SIGNUP FORM
  form = UserCreationForm()
  context = {
    'form': form,
    'error_message': error_message
  }
  return render(request, 'registration/signup.html', context)

