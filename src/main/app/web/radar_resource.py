from __future__ import annotations

from dependency_injector.wiring import inject, Provide
from flask import jsonify, Response
from flask_restx import Resource
from uuid import UUID

from main.app.common.validators import UuidValidator
from main.app.use_cases import UseCases, GetRadarUseCase
from main.app.web import org_namespace


@org_namespace.doc('class')
@org_namespace.route('/<string:organization_id>/radar')
class RadarResource(Resource):

    @org_namespace.doc('get metrics on risk factors for an organisation')
    @inject
    def get(
            self: RadarResource,
            organization_id: str,
            get_radar_use_case: GetRadarUseCase = Provide[UseCases.get_radar_use_case]
    ) -> Response:
        print('Rest call => GET Radar resource')
        UuidValidator.validate(organization_id)
        return jsonify(get_radar_use_case.execute(UUID(organization_id)))
