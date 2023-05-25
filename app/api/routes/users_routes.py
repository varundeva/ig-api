from flask import Blueprint
from app.api.controllers import getMetaData,getProfilePhoto

users_blueprint = Blueprint('users', __name__)

@users_blueprint.route('/profile-pic/<string:userName>', methods=['GET'])
def getUserProfilePhoto(userName):
    return getProfilePhoto(userName)

@users_blueprint.route('/<string:userName>', methods=['GET'])
def getUserMetaDataRoute(userName):
    return getMetaData(userName)