from dataclasses import dataclass
from uuid import UUID


@dataclass
class RiskFactorDto:
    id: UUID
    name: str
    impact: str
    probability: float
