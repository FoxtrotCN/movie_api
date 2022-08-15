from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Movie


class MovieList(ListView):
    model = Movie


class MovieDetail(DetailView):
    model = Movie


class MovieCreate(CreateView):
    model = Movie
    fields = ['title', 'synopsis', 'genre']
    success_url = reverse_lazy('movies')


class MovieUpdate(UpdateView):
    model = Movie
    fields = ['title', 'synopsis', 'genre']
    success_url = reverse_lazy('movie')


class MovieDelete(DeleteView):
    model = Movie
    context_object_name = 'movie'
    success_url = reverse_lazy('movies')
