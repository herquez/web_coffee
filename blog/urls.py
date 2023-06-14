from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('category/<category_id>', views.category, name='category')
]