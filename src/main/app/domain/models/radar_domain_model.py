from uuid import UUID


class RadarDomainModel:
    def __init__(
            self,
            risk_factor_id: UUID,
            risk_factor_name: str,
            priority_score: int
    ) -> None:
        self.risk_factor_id = risk_factor_id
        self.risk_factor_name = risk_factor_name
        self.average_priority_score = priority_score
