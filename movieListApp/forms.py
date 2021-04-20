from django import forms
from django.forms import DateInput, SelectDateWidget
from django.utils import timezone


class DateInput(forms.DateInput):
    input_type = 'date'


class MovieForm(forms.Form):
    title = forms.CharField(max_length=150,
                            label='Name of the movie',
                            widget=forms.TextInput(attrs={'class': 'form-control'}))


class UpdateMovieForm(forms.Form):
    director = forms.CharField(max_length=150,
                               label='Name of the director',
                               widget=forms.TextInput(attrs={'class': "form-control"}))
    genre = forms.CharField(max_length=150,
                            label='Name of the genre',
                            widget=forms.TextInput(attrs={'class': "form-control"}))
    releasedYear = forms.DateField(label='Released year', widget=DateInput(attrs={'class': "form-control"}))
