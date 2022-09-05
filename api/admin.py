from django.contrib import admin
from .models import Movie, Actor


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'synopsis', 'genre', 'tag')


class ActorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'role')


admin.site.register(Movie, MovieAdmin)
admin.site.register(Actor, ActorAdmin)
