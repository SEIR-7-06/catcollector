from django.db import models

# Create your models here.
class Cat:
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

felix = Cat('Felix', 'ally cat', 'Likes causing trouble', 3)
mittins = Cat('Mittins', 'calico', 'Very friendly', 1)
tigger = Cat('Tigger', 'tiger', 'Likes to bounce', 6)

cats = [
  felix,
  mittins,
  tigger
]