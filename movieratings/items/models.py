from django.db import models


class Movie(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=150)
    rel_date = models.DateTimeField('date release')
    imdb_url = models.CharField(max_length=200)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Rater(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=1)
    occupation = models.CharField(max_length=150)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return self.id


class Rating(models.Model):
    rater = models.ForeignKey(Rater, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.movie
