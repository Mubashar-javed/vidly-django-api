from rest_framework import generics
from rest_framework import viewsets

from movies.models import Movie, Genre
from .serializer import MovieSerializer, GenreSerializer


# todo : create endpoint for update movie
# todo : Update README.md file
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    # def create(self, request, *args, **kwargs):
    #     data = request.data.copy()
    #     genre = Genre.objects.get(_id=data.pop('genreId'))
    #     data = dict(**data, genre={"name": genre.name})
    #     serializer = self.get_serializer(data=data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class GenreApiView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
