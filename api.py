from flask import Blueprint, jsonify, request
from models import Movies

api = Blueprint('api', __name__)


@api.route('/api/movies/<int:id>', methods=['GET'])
def get_movie(id):
    movie = Movies.get(id)
    return jsonify(movie.to_dict())


@api.route('/api/movies/create', methods=['POST'])
def create_movie():
    if not request.is_json:
        return 'You should send JSON data', 400
    data = request.json
    if type(data) == list:
        return 'You should send JSON dictionary', 400
    if 'title' not in data:
        return '"Title" field is required', 400
    title = data.get('title')
    year = data.get('year')
    movie = Movies.create(title=title, year=year)

    return jsonify(movie.to_dict()), 201


@api.route('/api/movies/update/<int:id>', methods=['PUT'])
def update_movie(id):
    movie = Movies.get(id)
    movie.title = 'New_title'
    movie.year = 2021
    return jsonify(movie.to_dict())


@api.route('/api/movies/delete/<int:id>', methods=['DELETE'])
def delete_movie(id):
    movie = Movies.get(id)
    movie.delete()
    return jsonify({'result': True})
