from .views import MovieApiView, GenreApiView
from django.urls import path

urlpatterns = [
    path('movies', MovieApiView.as_view()),
    path('genres', GenreApiView.as_view())
]
