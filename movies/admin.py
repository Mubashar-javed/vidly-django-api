from django.contrib import admin
from .models import Genre, Movie


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'dailyRentalRate', "numberInStock"]
    list_editable = ["dailyRentalRate"]
    search_fields = ["title", "numberInStock"]
