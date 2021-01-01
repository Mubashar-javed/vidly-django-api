from .models import Genre, Movie
from rest_framework import serializers


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()

    class Meta:
        model = Movie
        fields = ["_id", "title", "genre", "numberInStock", "dailyRentalRate"]

    def create(self, validated_data):
        print("validated data is:", validated_data)
        return super().create(validated_data)
