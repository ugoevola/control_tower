from __future__ import annotations

from dependency_injector.wiring import inject, Provide
from typing import List
from uuid import UUID
from werkzeug.exceptions import NotFound

from main.app.common.dto import RadarDto
from main.app.common.mappers import RadarMapper
from main.app.domain import Domain
from main.app.domain.dao import RiskFactorPriorityDao


class GetRadarUseCase:

    @inject
    def execute(
            self: GetRadarUseCase,
            organization_id: UUID,
            risk_factor_priority_dao: RiskFactorPriorityDao = Provide[Domain.risk_factor_priority_dao]
    ) -> List[RadarDto]:
        radar_domain_model = risk_factor_priority_dao.get_average_priority_scores(organization_id)
        if not radar_domain_model:
            raise NotFound(f"no results were found for the organisation {organization_id}")
        return RadarMapper.map_domain_models_to_dto(radar_domain_model)
