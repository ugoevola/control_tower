from __future__ import annotations

from dependency_injector.wiring import inject, Provide
from flask_sqlalchemy import SQLAlchemy
from typing import List
from uuid import UUID

from main.app.common import GET_AVERAGE_PRIORITY_SCORES_REQUEST
from main.app.common.clients import Clients
from main.app.domain.models import RadarDomainModel


class RiskFactorPriorityDao:

    @inject
    def get_average_priority_scores(
            self: RiskFactorPriorityDao,
            organization_id: UUID,
            db_client: SQLAlchemy = Provide[Clients.db_client]
    ) -> List[RadarDomainModel]:
        query = GET_AVERAGE_PRIORITY_SCORES_REQUEST
        result = db_client.session.execute(query, {'organization_id': organization_id}).fetchall()
        return [RadarDomainModel(
            risk_factor_id=row[0],
            risk_factor_name=row[1],
            priority_score=row[2]
        ) for row in result]
