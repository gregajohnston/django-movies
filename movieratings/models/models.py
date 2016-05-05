from django.db import models


class Movie(models.Model):
    movie_id = models.CharField(max_length=10)
    title = models.CharField(max_length=255)
    release_date = models.DateField(max_length=30)
    video_release_date = models.DateField(max_length=30)
    imdb_url = models.CharField(max_length=255)
    genre = models.CharField(max_length=1)


class Rater(models.Model):
    user_id = models.CharField(max_length=10)
    age = models.CharField(max_length=2)
    gender = models.CharField(max_length=1)
    occupation = models.CharField(max_length=255)


class Rating(models.Model):
    rater = models.ForeignKey(Rater, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.CharField(max_length=2)
