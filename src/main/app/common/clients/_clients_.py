from dependency_injector import containers, providers
from flask_sqlalchemy import SQLAlchemy


class Clients(containers.DeclarativeContainer):
    config = providers.Configuration()
    db_client = providers.Dependency(instance_of=SQLAlchemy)
