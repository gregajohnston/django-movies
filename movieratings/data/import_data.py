import pandas as pd
from ../items/models import Movie, Rater, Rating


def read_user_data():
    df = pd.read_csv("u.user", header=None)
    for row in df.iterrows():
        index, data = row
        Rater(data.tolist()).save()


def read_movie_data():
    df = pd.read_csv("u.item", header=None)
    for row in df.iterrows():
        index, data = row
        Movie(data.tolist()).save()


def read_rating_data():
    df = pd.read_csv("u.data", header=None)
    for row in df.iterrows():
        index, data = row
        Rating(data.tolist()).save()


def main():
    read_user_data()
    read_movie_data()
    read_rating_data()


if __name__ == '__main__':
    main()
