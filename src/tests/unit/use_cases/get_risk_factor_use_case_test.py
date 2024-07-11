from __future__ import annotations

from pytest import raises
from werkzeug.exceptions import NotFound

from tests.unit.data import (
    get_risk_factor_ok,
    get_risk_factor_id_ok,
    get_risk_factor_dto_ok,
    get_risk_factor_id_not_found
)
from tests.unit.main_unit_test import *


def test_get_risk_factor_use_case_success(get_risk_factor_use_case, risk_factor_dao_mock):
    risk_factor_dao_mock.get_by_id.return_value = get_risk_factor_ok()

    expected_result = get_risk_factor_dto_ok()
    result = get_risk_factor_use_case.execute(get_risk_factor_id_ok())

    assert type(result) is type(expected_result)
    assert result == expected_result


def test_get_risk_factor_use_case_ko(get_risk_factor_use_case, risk_factor_dao_mock):
    risk_factor_dao_mock.get_by_id.return_value = None

    with raises(NotFound):
        get_risk_factor_use_case.execute(get_risk_factor_id_not_found())

