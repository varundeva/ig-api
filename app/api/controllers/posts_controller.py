from flask import jsonify

def get_posts():
    posts = [
        {'id': 1, 'title': 'Post 1'},
        {'id': 2, 'title': 'Post 2'},
        {'id': 3, 'title': 'Post 3'}
    ]
    return jsonify(posts)

def get_post(post_id):
    post = {'id': post_id, 'title': 'Post 1'}
    return jsonify(post)

def create_post(post_data):
    post = {'id': 4, 'title': post_data['title']}
    return jsonify(post)

def update_post(post_id, post_data):
    post = {'id': post_id, 'title': post_data['title']}
    return jsonify(post)

def delete_post(post_id):
    return jsonify({'message': 'Post deleted successfully'})
