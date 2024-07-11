from __future__ import annotations

from dependency_injector import containers, providers
from flask_restx import Api

from . import RiskFactorResource


class Resources(containers.DeclarativeContainer):
    config = providers.Configuration()
    risk_factor_resource = providers.Singleton(RiskFactorResource)
    api = providers.Dependency(instance_of=Api)


