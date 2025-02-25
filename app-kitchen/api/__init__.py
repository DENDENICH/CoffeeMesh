from flask_smorest import Blueprint

from .api_v1 import blueprint_api_v1


blueprint_api = Blueprint("main-api", __name__)
blueprint_api.register_blueprint(blueprint_api_v1)
