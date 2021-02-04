from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('cats/', views.cats_index, name='cats_index'),
  path('cats/<int:cat_id>/', views.cats_detail, name='cats_detail'),
  path('cat/<int:cat_id>/add_feeding/', views.add_feeding, name='add_feeding'),
  path('cats/<int:cat_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name="assoc_toy")
]

"""
app.use('/users/:userId', usersController);

app.get('/feeding', (req, res) => {

});

app.post('/feeding', req, res) => {

})


app.post('/cats/:catId/toys/:toyId', req, res) => {

})
"""
