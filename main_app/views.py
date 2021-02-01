from django.shortcuts import render
from django.http import HttpResponse

fav_colors = [
  'red',
  'green',
  'blue'
]

# Create your views here.
def home(request):
  # return HttpResponse('<h1>Welcome to Cat Collector</h1>')
  return render(request, 'home.html')

def about(request):
  # return HttpResponse('<h1>All about the Cat Collector</h1>')
  return render(request, 'about.html')