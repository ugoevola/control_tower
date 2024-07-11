from typing import List

from main.app.common.dto import RadarDto
from main.app.domain.models import RadarDomainModel


class RadarMapper:

    @staticmethod
    def map_domain_models_to_dto(
            domain_models: List[RadarDomainModel]
    ) -> List[RadarDto]:
        return [RadarDto(
            risk_factor_id=row.risk_factor_id,
            risk_factor_name=row.risk_factor_name,
            priority_score=row.average_priority_score
        ) for row in domain_models]
