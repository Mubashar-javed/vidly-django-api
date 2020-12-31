from rest_framework import generics

from movies.models import Movie, Genre
from .serializer import MovieSerializer, GenreSerializer


class MovieApiView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class GenreApiView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
