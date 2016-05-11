from django.db import models


class Movie(models.Model):
    movie_id = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=150)
    date_added = models.DateField('date added')
    imdb_url = models.CharField(max_length=200)
    genre_1 = models.CharField(max_length=50, default=0)
    genre_2 = models.CharField(max_length=50, default=0)
    genre_3 = models.CharField(max_length=50, default=0)
    genre_4 = models.CharField(max_length=50, default=0)
    genre_5 = models.CharField(max_length=50, default=0)
    genre_6 = models.CharField(max_length=50, default=0)
    genre_7 = models.CharField(max_length=50, default=0)
    genre_8 = models.CharField(max_length=50, default=0)
    genre_9 = models.CharField(max_length=50, default=0)
    genre_10 = models.CharField(max_length=50, default=0)
    genre_11 = models.CharField(max_length=50, default=0)
    genre_12 = models.CharField(max_length=50, default=0)
    genre_13 = models.CharField(max_length=50, default=0)
    genre_14 = models.CharField(max_length=50, default=0)
    genre_15 = models.CharField(max_length=50, default=0)
    genre_16 = models.CharField(max_length=50, default=0)
    genre_17 = models.CharField(max_length=50, default=0)
    genre_18 = models.CharField(max_length=50, default=0)
    genre_19 = models.CharField(max_length=50, default=0)
    genre_20 = models.CharField(max_length=50, default=0)

    def __str__(self):
        return self.title


class Rater(models.Model):
    rater_id = models.CharField(max_length=20, primary_key=True)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=1)
    occupation = models.CharField(max_length=150)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return self.id


class Rating(models.Model):
    movie_id = models.CharField(max_length=20, default=0)
    rater_id = models.CharField(max_length=20, default=0)
    # movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE, default=0)
    # rater_id = models.ForeignKey(Rater, on_delete=models.CASCADE, default=0)
    rating = models.IntegerField(default=0)
    timestamp = models.IntegerField(default=0)
