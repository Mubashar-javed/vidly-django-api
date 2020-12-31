from rest_framework import generics

from movies.models import Movie
from .serializer import MovieSerializer


class MovieApiView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
