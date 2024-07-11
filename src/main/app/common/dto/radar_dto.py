from dataclasses import dataclass
from uuid import UUID


@dataclass
class RadarDto:
    risk_factor_id: UUID
    risk_factor_name: str
    priority_score: int
