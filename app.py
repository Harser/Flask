from flask import Flask
from models import Movies
import random

app = Flask(__name__)


@app.route('/')
def hello_world():
    movies = Movies.select()
    movies_str = []
    for i in range(10):
        movie = random.choice(movies)  # type: Movies
        movies_str.append(f'{movie.id}. {movie.title} ({movie.year})')
    return '<br>'.join(movies_str)


if __name__ == '__main__':
    app.run()
