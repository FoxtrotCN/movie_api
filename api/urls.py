from django.urls import path
from .views import *

urlpatterns = [
    path('movies/', MovieList.as_view(), name='movies'),
    path('movies/<str:pk>/', MovieDetail.as_view(), name='movie'),
    path('create-movie/', MovieCreate.as_view(), name='create-movie'),
    path('update-movie/<str:pk>/', MovieUpdate.as_view(), name='update-movie'),
    path('delete-movie/<str:pk>/', MovieDelete.as_view(), name='delete-movie'),
]
