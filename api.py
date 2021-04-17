from flask import Blueprint, jsonify, request
from models import Movies

api = Blueprint('api', __name__)


@api.route('/api/movies/<int:id>', methods=['GET'])
def get_movie(id):
    movie = Movies.get(id)
    return jsonify(movie.to_dict())


@api.route('/api/movies/create', methods=['POST'])
def create_movie():
    print(request.data)
    return "Yes"


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
