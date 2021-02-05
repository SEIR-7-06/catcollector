from django.db import models
from django.contrib.auth.models import User

class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return f'{self.name} color {self.color}'

class Cat(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  toys = models.ManyToManyField(Toy, blank=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  # No need to make migration for model methods
  def __str__(self):
    return self.name


MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner')
)

class Feeding(models.Model):
  date = models.DateField()
  meal = models.CharField(
    max_length=1,
    choices=MEALS,
    default=MEALS[0][0]
  )
  cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.get_meal_display()} on {self.date}'
