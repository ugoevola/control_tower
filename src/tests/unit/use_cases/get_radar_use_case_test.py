from __future__ import annotations

from pytest import raises
from werkzeug.exceptions import NotFound

from tests.unit.data import (
    get_radar_domain_model_list_ok,
    get_radar_dto_list_ok,
    get_organisation_id_ok,
    get_organisation_id_not_found
)
from tests.unit.main_unit_test import *


def test_get_radar_use_case_success(get_radar_use_case, risk_factor_priority_dao_mock):
    risk_factor_priority_dao_mock.get_average_priority_scores.return_value = get_radar_domain_model_list_ok()

    result = get_radar_use_case.execute(get_organisation_id_ok())

    assert isinstance(result, list)
    assert len(result) == len(get_radar_dto_list_ok())
    assert result == get_radar_dto_list_ok()


def test_get_radar_use_case_ko(get_radar_use_case, risk_factor_priority_dao_mock):
    risk_factor_priority_dao_mock.get_average_priority_scores.return_value = []

    with raises(NotFound):
        get_radar_use_case.execute(get_organisation_id_not_found())

