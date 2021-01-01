from .models import Genre, Movie
from rest_framework import serializers


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["_id", "name"]


class MovieSerializer(serializers.ModelSerializer):
    # genre = GenreSerializer()

    class Meta:
        model = Movie
        fields = ["_id", "title", "genre", "numberInStock", "dailyRentalRate"]
