from __future__ import annotations

from dependency_injector.wiring import inject, Provide
from flask import jsonify, Response
from flask_restx import Resource
from uuid import UUID

from main.app.web import risk_factor_namespace
from main.app.common.validators import UuidValidator
from main.app.use_cases import UseCases, GetRiskFactorUseCase


@risk_factor_namespace.doc('class')
@risk_factor_namespace.route('/<string:risk_factor_id>')
class RiskFactorResource(Resource):

    @risk_factor_namespace.doc('get a risk factor by id')
    @inject
    def get(
            self: RiskFactorResource,
            risk_factor_id: str,
            get_risk_factor_use_case: GetRiskFactorUseCase = Provide[UseCases.get_risk_factor_use_case]
    ) -> Response:
        print('Rest call => GET risk factor')
        UuidValidator.validate(risk_factor_id)
        return jsonify(get_risk_factor_use_case.execute(UUID(risk_factor_id)))
