from django.db import models


class Genre(models.Model):
    _id = models.AutoField(primary_key=True)
    name = models.CharField("Genre Name", unique=True, max_length=50)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.name = self.name.strip()
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return str(self.name)


class Movie(models.Model):
    _id = models.AutoField(primary_key=True)
    title = models.CharField(unique=True, max_length=250)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    numberInStock = models.PositiveSmallIntegerField(default=0)
    dailyRentalRate = models.PositiveSmallIntegerField(default=0)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # remove title whitespaces before saving in db
        self.title = self.title.strip()
        return super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return str(self.title)
