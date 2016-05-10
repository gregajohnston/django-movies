import csv
import json
from datetime import date, datetime


MOVIE_COLUMNS = ['id', 'title', 'date_added', 'drop',
                 'imdb_url'] + ['genre_{}'.format(x) for x in range(1, 20)]
RATER_COLUMNS = ['id', 'age', 'gender', 'occupation', 'zip_code']
RATING_COLUMNS = ['rater_id', 'movie_id', 'rating', 'timestamp']

MOVIE_FILE = 'data/u.item'
RATER_FILE = 'data/u.user'
RATING_FILE = 'data/u.data'

MOVIE_MODEL = 'items.movie'
RATER_MODEL = 'items.rater'
RATING_MODEL = 'items.rating'

MOVIE_JSON = 'items/fixtures/movie.json'
RATER_JSON = 'items/fixtures/rater.json'
RATING_JSON = 'items/fixtures/rating.json'


def read_data(input_file, output_file, column_names, model_name):
    with open(output_file, 'w+') as j:
        with open(input_file, encoding='latin_1') as f:
            delim = '|'
            if input_file == 'data/u.data':
                delim = '\t'
            reader = csv.DictReader(f, fieldnames=column_names,
                                    delimiter=delim)
            output = "["
            counter = 0
            for row in reader:
                if input_file == 'data/u.item':
                    index_value = row['id']

                    date_added = row['date_added']
                    if date_added:
                        date_added = datetime.strptime(date_added, '%d-%b-%Y')
                    else:
                        date_added = date(1900, 1, 1)

                    row['date_added'] = date_added.strftime('%Y-%m-%d')

                    del row['drop']
                    del row['id']
                if input_file == 'data/u.user':
                    index_value = row['id']
                    del row['id']
                if input_file == 'data/u.data':
                    counter += 1
                    index_value = counter
                output += "{" + "\"model\": \"{}\", \"pk\": {}, ".format(
                            model_name, index_value)
                output += "\"fields\": {}".format(json.dumps(row)) + "}, "
            output = output[:-2]
            output += "]"
            j.write(output)


def main():
    read_data(MOVIE_FILE, MOVIE_JSON, MOVIE_COLUMNS, MOVIE_MODEL)
    read_data(RATER_FILE, RATER_JSON, RATER_COLUMNS, RATER_MODEL)
    read_data(RATING_FILE, RATING_JSON, RATING_COLUMNS, RATING_MODEL)

if __name__ == '__main__':
    main()
