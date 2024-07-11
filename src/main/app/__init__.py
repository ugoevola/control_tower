import importlib.resources as resources
import yaml

from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from typing import Optional


def get_config():
    resource_path = resources.files('main').joinpath('resources/config.yml')
    with resource_path.open('r') as file:
        return yaml.load(file, Loader=yaml.FullLoader)


config = get_config()

app: Optional[Flask] = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = config.get('database').get('uri')


db_client: Optional[SQLAlchemy] = SQLAlchemy()
db_client.init_app(app)


api: Optional[Api] = Api(
    app=app,
    title=config.get('api').get('title'),
    description=config.get('api').get('description'),
    version=config.get('api').get('version'),
)
