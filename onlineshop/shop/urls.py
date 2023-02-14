from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='main'),
    path('cats/<int:catid>/', categories, name='cats'),
    path('about/', about, name='about')
]