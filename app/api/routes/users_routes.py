from flask import Blueprint, request
from app.api.controllers import get_users, get_user, create_user, update_user, delete_user

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/', methods=['GET'])
def get_all_users():
    return get_users()

@users_blueprint.route('/<int:user_id>', methods=['GET'])
def get_single_user(user_id):
    return get_user(user_id)

@users_blueprint.route('/', methods=['POST'])
def create_new_user():
    user_data = request.get_json()
    return create_user(user_data)

@users_blueprint.route('/<int:user_id>', methods=['PUT'])
def update_existing_user(user_id):
    user_data = request.get_json()
    return update_user(user_id, user_data)

@users_blueprint.route('/<int:user_id>', methods=['DELETE'])
def delete_existing_user(user_id):
    return delete_user(user_id)
