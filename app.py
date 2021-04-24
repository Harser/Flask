from flask import Flask, render_template
import random

from models import Movies, Users
from api.movies_api import movies_api
from api.users_api import users_api

app = Flask(__name__)
app.register_blueprint(movies_api)
app.register_blueprint(users_api)


@app.route('/')
def index():
    # 10 randomly chosen movies
    movies = random.sample(list(Movies.select()), 10)
    return render_template('index.html', movies=movies)


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


@app.route('/users/<int:id>')
def user(id):
    user = Users.get(id)
    return render_template('users.html', user=user)


if __name__ == '__main__':
    app.run(debug=True)
