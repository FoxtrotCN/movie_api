from django.urls import path
from .views import *

urlpatterns = [
    path('movies/', MovieView.as_view(), name='movies-list'),
    path('create-new-movie/', MovieView.as_view(), name='create-new-movie'),
    path('movie-detail/<int:pk>/', MovieView.as_view(), name='movie-detail'),
    path('update-movie/<int:pk>/', MovieView.as_view(), name='update-movie'),
    path('delete-movie/<int:pk>/', MovieView.as_view(), name='delete-movie'),

]
