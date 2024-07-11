import uuid

from main.app import db_client


class RiskFactorPriority(db_client.Model):
    __tablename__ = 'risk_factor_priority'

    organization_id = db_client.Column(db_client.String(36), default=lambda: str(uuid.uuid4()))
    project_id = db_client.Column(db_client.String(36), default=lambda: str(uuid.uuid4()))
    project_evaluation_id = db_client.Column(db_client.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    risk_factor_id = db_client.Column(db_client.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    risk_priority_score = db_client.Column(db_client.Integer, nullable=True)
    is_project_evaluation_last = db_client.Column(db_client.Boolean, nullable=True)

    def __repr__(self):
        return f'<RiskFactorPriority {self.project_evaluation_id} {self.risk_factor_id}>'
