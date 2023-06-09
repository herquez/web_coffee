from django.contrib import admin
from django.urls import path
from core import views as views_core

urlpatterns = [
    path('', views_core.home, name='home'),
    path('about/', views_core.about, name='about'),
    path('services/', views_core.services, name='services'),
    path('store/', views_core.store, name='store'),
    path('contact/', views_core.contact, name='contact'),
    path('blog/', views_core.blog, name='blog'),
    path('sample/', views_core.sample, name='sample'),
    path('admin/', admin.site.urls),
]
