import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vidly.settings')
django.setup()
# import will only works after django.setup()
from movies.models import Genre, Movie

# copied from vidly-node-api
data = [
    {
        "name": "Comedy",
        "movies": [
            {"title": "Airplane", "numberInStock": 5, "dailyRentalRate": 2},
            {"title": "The Hangover", "numberInStock": 10, "dailyRentalRate": 2},
            {"title": "Wedding Crashers", "numberInStock": 15, "dailyRentalRate": 2}
        ]
    },
    {
        "name": "Action",
        "movies": [
            {"title": "Die Hard", "numberInStock": 5, "dailyRentalRate": 2},
            {"title": "Terminator", "numberInStock": 10, "dailyRentalRate": 2},
            {"title": "The Avengers", "numberInStock": 15, "dailyRentalRate": 2}
        ]
    },
    {
        "name": "Romance",
        "movies": [
            {"title": "The Notebook", "numberInStock": 5, "dailyRentalRate": 2},
            {"title": "When Harry Met Sally", "numberInStock": 10, "dailyRentalRate": 2},
            {"title": "Pretty Woman", "numberInStock": 15, "dailyRentalRate": 2}
        ]
    },
    {
        "name": "Thriller",
        "movies": [
            {"title": "The Sixth Sense", "numberInStock": 5, "dailyRentalRate": 2},
            {"title": "Gone Girl", "numberInStock": 10, "dailyRentalRate": 2},
            {"title": "The Others", "numberInStock": 15, "dailyRentalRate": 2}
        ]
    }
]

for m in data:
    genreName = m.get('name').strip()
    genre, created = Genre.objects.get_or_create(name=genreName)
    for movie in m.get('movies'):
        Movie.objects.create(**movie, genre=genre, )

print("done!")
