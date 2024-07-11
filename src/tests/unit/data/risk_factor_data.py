from uuid import UUID

from main.app.domain.entities import RiskFactor


def get_risk_factor_ok():
    return RiskFactor(
        id=UUID("9930919d-e316-4db7-a326-559289dc069b"),
        name="Problèmes de financement",
        probability=0.6,
        impact="modéré"
    )


def get_risk_factor_id_ok():
    return "9930919d-e316-4db7-a326-559289dc069b"


def get_risk_factor_id_not_found():
    return "995fe37f-c629-4ff5-98af-f5afb82fcca2"
