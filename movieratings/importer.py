import csv
import json


MOVIE_COLUMNS = ['movie_id', 'movie_title', 'date_added',
                 'imdb_url'] + ['genre {}'.format(x) for x in range(19)]
RATER_COLUMNS = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
RATING_COLUMNS = ['user_id', 'movie_id', 'rating', 'timestamp']

MOVIE_FILE = 'data/u.item'
RATER_FILE = 'data/u.user'
RATING_FILE = 'data/u.data'

MOVIE_JSON = 'items/movie.json'
RATER_JSON = 'items/rater.json'
RATING_JSON = 'items/rating.json'


def read_data(input_file, output_file, column_names):
    with open(output_file, 'w+') as j:
        with open(input_file, encoding='latin_1') as f:
            reader = csv.DictReader(f, fieldnames=column_names, delimiter='|')
            output = json.dumps([row for row in reader])
        j.write(output)


def main():
    read_data(MOVIE_FILE, MOVIE_JSON, MOVIE_COLUMNS)
    read_data(RATER_FILE, RATER_JSON, RATER_COLUMNS)
    read_data(RATING_FILE, RATING_JSON, RATING_COLUMNS)

if __name__ == '__main__':
    main()
