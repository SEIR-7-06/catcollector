from django.urls import path
from . import views

print(views.fav_colors)

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about')
]

"""
app.use('/users', usersController);
"""