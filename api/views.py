from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import View
from django.http.response import JsonResponse
from .models import Movie
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json


class MovieView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, pk=0):
        """
        Return the list of all movies, or a single movie
        :param pk:
        :param request:
        :return:
        """
        if pk > 0:
            movies = list(Movie.objects.filter(pk=pk).values())
            if len(movies) > 0:
                movie = movies[0]
                data = {'message': "Success", 'movie': movie}
            else:
                data = {'message': "Movie not found... "}
            return JsonResponse(data)
        else:

            movies = list(Movie.objects.values().order_by('pk'))
            if len(movies) > 0:
                data = {'message': "Success", 'movies': movies}
            else:
                data = {'message': "Movies not found ..."}
            return JsonResponse(data)

    def post(self, request):
        """
        Create a new movie
        :param request:
        :return:
        """
        json_data = json.loads(request.body)
        Movie.objects.create(title=json_data['title'], synopsis=json_data['synopsis'], genre=json_data['genre'],
                             tag=json_data['tag'])
        data = {'message': "Success"}
        return JsonResponse(data)

    def put(self, request, pk):
        """
        Update a single movie
        :param request:
        :param pk:
        :return:
        """
        json_data = json.loads(request.body)
        movies = list(Movie.objects.filter(pk=pk).values())
        if len(movies) > 0:
            movie = Movie.objects.get(pk=pk)
            movie.title = json_data['title']
            movie.synopsis = json_data['synopsis']
            movie.genre = json_data['genre']
            movie.tag = json_data['tag']
            movie.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Movie not found ..."}
        return JsonResponse(data)

    def delete(self, request, pk):
        movies = list(Movie.objects.filter(pk=pk).values())
        if len(movies) > 0:
            Movie.objects.filter(pk=pk).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Movie not found ..."}
        return JsonResponse(data)
