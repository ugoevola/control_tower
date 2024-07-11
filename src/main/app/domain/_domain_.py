from dependency_injector import containers, providers

from .dao import RiskFactorDao


class Domain(containers.DeclarativeContainer):
    config = providers.Configuration()
    risk_factor_dao = providers.Singleton(RiskFactorDao)
