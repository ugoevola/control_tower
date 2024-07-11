from main.app.domain.entities import RiskFactor


class RiskFactorDao:
    @staticmethod
    def get_by_id(risk_factor_id) -> RiskFactor:
        return RiskFactor.query.get(risk_factor_id)
