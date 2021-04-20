from django.db import models
from django.utils import timezone


class Movie(models.Model):
    movie_name = models.CharField(max_length=150)
    release_year = models.DateField(blank=True, null=True)
    director = models.CharField(max_length=150)
    genre = models.CharField(max_length=150)

    def __str__(self):
        return self.movie_name
