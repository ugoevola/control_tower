from __future__ import annotations

from dependency_injector.wiring import inject, Provide
from uuid import UUID
from werkzeug.exceptions import NotFound

from main.app.common.dto import RiskFactorDto
from main.app.common.mappers import RiskFactorMapper
from main.app.domain import Domain
from main.app.domain.dao import RiskFactorDao


class GetRiskFactorUseCase:

    @inject
    def execute(
            self: GetRiskFactorUseCase,
            risk_factor_id: UUID,
            risk_factor_dao: RiskFactorDao = Provide[Domain.risk_factor_dao]
    ) -> RiskFactorDto:
        risk_factor_domain_model = risk_factor_dao.get_by_id(risk_factor_id)
        if not risk_factor_domain_model:
            raise NotFound(f"no results were found for the id {risk_factor_id}")
        return RiskFactorMapper.map_entity_to_dto(risk_factor_domain_model)
