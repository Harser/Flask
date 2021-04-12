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