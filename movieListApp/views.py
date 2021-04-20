from datetime import datetime

import requests
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from movieListApp import models
from movieListApp.forms import MovieForm, UpdateMovieForm
from movieListApp.models import Movie


def index(request):
    movies = models.Movie.objects.all()
    context = {
        "movies": movies
    }
    return render(request, 'movieListApp/index.html', context)


def movie_detail(request, id):
    if request.method == 'POST':
        form = UpdateMovieForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            movie = models.Movie.objects.get(pk=id)
            movie.genre = data['genre']
            movie.director = data['director']
            movie.release_year = data['releasedYear']
            movie.save()
            return redirect('index')
    elif request.method == 'GET':
        movie = models.Movie.objects.get(pk=id)
        form = UpdateMovieForm(initial={
            'director': movie.director,
            'genre': movie.genre,
            'releasedYear': movie.release_year
        })
        context = {
            "movie": movie,
            "title": movie.movie_name,
            "form": form
        }
        return render(request, 'movieListApp/movie.html', context)


def movie_add(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            movie = requests.get("http://www.omdbapi.com/?t=" + data['title'] + "&apikey=c734f4").json()
            if movie['Response'] == 'True':
                formatted_date = datetime.strptime(movie['Released'], "%d %b %Y")
                new_movie = Movie(movie_name=movie['Title'],
                                  release_year=formatted_date,
                                  director=movie['Director'],
                                  genre=movie['Genre'])
                new_movie.save()
                return redirect('index')
            else:
                new_movie = Movie(movie_name=data['title'])
                new_movie.save()
                movie = models.Movie.objects.get(movie_name=data['title'])
                return redirect('movie', id=movie.id)
    elif request.method == 'GET':
        form = MovieForm()
        return render(request, 'movieListApp/addMovie.html', {"form": form})
