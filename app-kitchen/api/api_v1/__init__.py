from flask_smorest import Blueprint

from .kitchen import blueprint_kitchen


blueprint_api_v1 = Blueprint("v1", __name__)
blueprint_api_v1.register_blueprint(blueprint_kitchen)
