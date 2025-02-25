from flask import Flask
from flask_smorest import Api

from config import BaseConfig

from api import blueprint_api


app = Flask("main")
app.config.from_object(BaseConfig)

kitchen_api = Api(app=app)
kitchen_api.register_blueprint(blueprint_api)


if __name__ == "__main__":
    app.run(
        host="localhost", 
        port=7655,
    )