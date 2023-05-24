from flask import Blueprint

api_blueprint = Blueprint('api', __name__)

# Import the user_routes and posts_routes blueprints
from app.api.routes.users_routes import users_blueprint
from app.api.routes.posts_routes import posts_blueprint

# Register the blueprints
api_blueprint.register_blueprint(users_blueprint, url_prefix='/users')
api_blueprint.register_blueprint(posts_blueprint, url_prefix='/posts')

