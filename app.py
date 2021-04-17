from flask import Flask, render_template
from models import Movies
from api import api
import random

app = Flask(__name__)
app.register_blueprint(api)


@app.route('/')
def index():
    # 10 randomly chosen movies
    movies = random.sample(list(Movies.select()), 10)
    return render_template('index.html',  movies=movies)

@app.route('/page1')
def page1():
    return render_template('page1.html')


@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/movies/<int:id>')
def movie(id):
    movie = Movies.get(id)
    genres = list(movie.genres)
    return render_template('film_info.html', movie=movie, genres=genres)


if __name__ == '__main__':
    app.run(debug=True)