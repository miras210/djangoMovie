from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('movie/<int:id>/', movie_detail, name="movie"),
    path('movie/add/', movie_add, name="add_movie"),
]