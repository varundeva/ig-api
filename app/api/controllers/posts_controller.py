from flask import jsonify
from app.config import getIgConnection
from instaloader import Post
from app.api.utils import  getPostInfo

def getPostById(postId):
    conn = getIgConnection()
    try:
        post = Post.from_shortcode(conn, postId)
        return jsonify({
            'status': True,
            'data' : getPostInfo(post)
        }) , 200
    except Exception as e:

        return jsonify({
            'status': False,
            'message': 'Something went Wrong. Server Error or Profile Not Found',
            'error' : str(e)
        }) , 500
