from dependency_injector import containers, providers

from .dao import RiskFactorPriorityDao, RiskFactorDao


class Domain(containers.DeclarativeContainer):
    config = providers.Configuration()
    risk_factor_priority_dao = providers.Singleton(RiskFactorPriorityDao)
    risk_factor_dao = providers.Singleton(RiskFactorDao)
