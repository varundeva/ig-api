from flask import Blueprint, request
from app.api.controllers import get_post, get_posts,create_post,delete_post, update_post

posts_blueprint = Blueprint('posts', __name__)

@posts_blueprint.route('/', methods=['GET'])
def get_all_posts():
    return get_posts()

@posts_blueprint.route('/<int:post_id>', methods=['GET'])
def get_single_post(post_id):
    return get_post(post_id)

@posts_blueprint.route('/', methods=['POST'])
def create_new_post():
    post_data = request.get_json()
    return create_post(post_data)

@posts_blueprint.route('/<int:post_id>', methods=['PUT'])
def update_existing_post(post_id):
    post_data = request.get_json()
    return update_post(post_id, post_data)

@posts_blueprint.route('/<int:post_id>', methods=['DELETE'])
def delete_existing_post(post_id):
    return delete_post(post_id)
