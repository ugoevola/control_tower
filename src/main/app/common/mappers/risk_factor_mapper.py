from uuid import UUID

from main.app.common.dto import RiskFactorDto
from main.app.domain.entities import RiskFactor


class RiskFactorMapper:

    @staticmethod
    def map_entity_to_dto(
            entity: RiskFactor
    ) -> RiskFactorDto:
        return RiskFactorDto(
            id=entity.id,
            name=entity.name,
            impact=entity.impact,
            probability=entity.probability
        )
