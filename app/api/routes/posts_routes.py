from flask import Blueprint
from app.api.controllers import getPostById

posts_blueprint = Blueprint('posts', __name__)

@posts_blueprint.route('/download/<string:postId>', methods=['GET'])
def getPostData(postId):
    return getPostById(postId)
