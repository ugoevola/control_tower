from dependency_injector import containers, providers

from . import GetRiskFactorUseCase


class UseCases(containers.DeclarativeContainer):

    config = providers.Configuration()
    get_risk_factor_use_case = providers.Singleton(GetRiskFactorUseCase)
