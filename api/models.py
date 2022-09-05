from django.db import models


class Actor(models.Model):
    full_name = models.CharField(max_length=125)
    role = models.CharField(max_length=125)

    def __str__(self):
        return self.full_name


class Movie(models.Model):
    ACTION = 'AC'
    DRAMA = 'DR'
    COMEDY = 'CM'
    SCIENCE_FICTION = 'SF'
    THRILLER = 'TR'
    RELIGIOUS = 'RG'

    GENRE_CHOICES = [

        (ACTION, 'Accion'),
        (DRAMA, 'Drama'),
        (COMEDY, 'Comedy'),
        (SCIENCE_FICTION, 'Ciencia Ficcion'),
        (THRILLER, 'Triler'),
        (RELIGIOUS, 'Religioso')
    ]

    title = models.CharField(max_length=155, blank=False)
    synopsis = models.TextField(max_length=1000, blank=True)
    genre = models.CharField(max_length=100, choices=GENRE_CHOICES, default='', blank=False)
    tag = models.JSONField(default=dict, blank=True)
    actors = models.ManyToManyField(Actor, related_name='movies', blank=True)

    def __str__(self):
        return self.title

    @classmethod
    def find_all_movies(cls):
        movies = Movie.objects.filter(actors__isnull=False).distinct().order_by('pk')
        movie_list = []
        for movie in movies:
            movie_list.append({
                "title": movie.title,
                "synopsis": movie.synopsis,
                "genre": movie.genre,
                "tag": movie.tag,
                "actors": list(movie.actors.all().values('full_name', 'role'))
            })

        return movie_list











    # def serialize(self):
    #     return {
    #         'title': self.title,
    #         'synopsis': self.synopsis,
    #         'genre': self.genre
    #     }
