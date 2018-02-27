from django.db import models


class Movie(models.Model):
    title = models.CharField(unique=True, max_length=50)
    description = models.TextField()
    release_date = models.DateTimeField()
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)


class Genre(models.Model):
    name = models.CharField(unique=True, max_length=50)
