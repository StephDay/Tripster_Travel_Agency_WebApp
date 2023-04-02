from django.contrib import admin
from django.urls import path
from . import views

app_name = 'a_django_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls, name='admin'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('packages/', views.packages, name='packages'),
    path('package/<int:pk>/', views.package_detail, name='package_detail'),
]