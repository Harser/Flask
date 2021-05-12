from flask import Blueprint, jsonify, request
from models import Users

users_api = Blueprint('users_api', __name__)


@users_api.route('/api/users/<int:id>', methods=['GET'])
def get_movie(id):
    user = Users.get(id)
    return jsonify(user.to_dict())


@users_api.route('/api/users/create', methods=['POST'])
def create_movie():
    if not request.is_json:
        return 'You should send JSON data', 400
    data = request.json
    if type(data) == list:
        return 'You should send JSON dictionary', 400
    if 'name' not in data:
        return '"Name" field is required', 400
    name = data.get('name')
    user = Users.create(name=name)
    return jsonify(user.to_dict()), 201


@users_api.route('/api/users/update/<int:id>', methods=['PUT'])
def update_movie(id):
    data = request.json
    user = Users.get(id)
    user.name = data.get('user', user.name)
    user.save()
    return jsonify(user.to_dict())
 

@users_api.route('/api/users/delete/<int:id>', methods=['DELETE'])
def delete_movie(id):
    Users.delete_by_id(id)
    return ""


@users_api.route('/api/users/update/<int:id>', methods=['POST'])
def update_user_from_form(id):
    print(id, request.form)
    return "Hello world"
