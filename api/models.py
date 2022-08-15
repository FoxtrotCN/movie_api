from django.db import models


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

    def __str__(self):
        return self.title

    # def serialize(self):
    #     return {
    #         'title': self.title,
    #         'synopsis': self.synopsis,
    #         'genre': self.genre
    #     }
