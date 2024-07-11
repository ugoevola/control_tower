from __future__ import annotations

from flask_sqlalchemy import SQLAlchemy
from dependency_injector import containers, providers
from flask_restx import Api

from main.app.common.clients import Clients
from main.app.domain import Domain
from main.app.use_cases import UseCases
from main.app.web import Resources


class AppContainer(containers.DeclarativeContainer):

    config = providers.Configuration()
    db_client = providers.Dependency(instance_of=SQLAlchemy)
    api = providers.Dependency(instance_of=Api)

    clients = providers.Container(
        Clients,
        config=config.clients,
        db_client=db_client
    )

    domain = providers.Container(
        Domain,
        config=config.domain
    )

    use_cases = providers.Container(
        UseCases,
        config=config.usescases
    )

    resources = providers.Container(
        Resources,
        config=config.resources,
        api=api
    )
