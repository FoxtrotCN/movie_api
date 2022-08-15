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


class MovieList(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, pk):
        """
        Return a List of all Movies, or a Single movie
        :param request:
        :param pk:
        :return:
        """
        if pk:
            movies = list(Movie.objects.filter(pk=pk).values())
            if len(movies) > 0:
                movie = movies[0]
                data = {'message': "Success", 'movie': movie}
            else:
                data = {'message': "Movie not found ..."}
            return JsonResponse(data)

        else:

            movies = list(Movie.objects.values())
            if len(movies) > 0:
                data = {'message': "Success", 'movies': movies}
            else:
                data = {'message': "Movies not found"}
            return JsonResponse(data)

    def post(self, request):

        json_data = json.loads(request.body)
        Movie.objects.create(title=json_data['title'], synopsis=json_data['synopsis'], genre=json_data['genre'])
        data = {'message': "Success"}
        return JsonResponse(data)

    def put(self, request):
        pass

    def delete(self, request):
        pass
