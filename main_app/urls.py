from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('cats/', views.cats_index, name='cats_index'),
  path('cats/<int:cat_id>/', views.cats_detail, name='cats_detail'),

  # Delete Cat
  path('cats/<int:cat_id>/delete/', views.delete_cat, name='delete_cat'),

  # Edit Cat
  path('cats/<int:cat_id>/edit', views.edit_cat, name='edit_cat'),

  path('cat/<int:cat_id>/add_feeding/', views.add_feeding, name='add_feeding'),
  path('cats/<int:cat_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name="assoc_toy"),

  # Auth Paths
  path('accounts/signup/', views.signup, name='signup')
]

"""
app.get('/users/:userId', usersController);
app.post('/users/:userId', usersController);

app.get('/feeding', (req, res) => {

});

app.post('/feeding', req, res) => {

})


app.post('/cats/:catId/toys/:toyId', req, res) => {

})
"""
