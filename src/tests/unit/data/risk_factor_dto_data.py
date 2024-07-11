from uuid import UUID

from main.app.common.dto import RiskFactorDto


def get_risk_factor_dto_ok():
    return RiskFactorDto(
        id=UUID("9930919d-e316-4db7-a326-559289dc069b"),
        name="Problèmes de financement",
        probability=0.6,
        impact="modéré"
    )
