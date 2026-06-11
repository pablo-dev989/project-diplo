from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    pub_date = models.DateField('date published')