from django.urls import path
from . import views

urlpatterns = [
    path('', views.website_list, name='website_list'),
    path('add/', views.add_website, name='add_website'),
]