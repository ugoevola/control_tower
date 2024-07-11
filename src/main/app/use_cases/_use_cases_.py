from dependency_injector import containers, providers

from . import GetRadarUseCase, GetRiskFactorUseCase


class UseCases(containers.DeclarativeContainer):

    config = providers.Configuration()
    get_radar_use_case = providers.Singleton(GetRadarUseCase)
    get_risk_factor_use_case = providers.Singleton(GetRiskFactorUseCase)
