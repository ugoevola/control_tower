import uuid

from main.app import db_client


class RiskFactor(db_client.Model):
    id = db_client.Column(db_client.String(36), primary_key=True, default=str(uuid.uuid4()))
    name = db_client.Column(db_client.String(255), nullable=False)
    probability = db_client.Column(db_client.Numeric(precision=3, scale=2), nullable=False)
    impact = db_client.Column(db_client.Text)

    __table_args__ = (
        db_client.CheckConstraint('probability >= 0 AND probability <= 1'),
    )
