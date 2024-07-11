from __future__ import annotations

import pytest
from unittest.mock import Mock
from main.app.app_container import AppContainer
from main.app.use_cases import GetRiskFactorUseCase


# dao mocks
@pytest.fixture(scope='module', autouse=True)
def risk_factor_dao_mock():
    mock = Mock()
    yield mock


# use cases
@pytest.fixture(scope='module', autouse=True)
def get_risk_factor_use_case():
    return GetRiskFactorUseCase()


@pytest.fixture(scope='module', autouse=True)
def container(risk_factor_dao_mock):
    container = AppContainer()
    container.init_resources()
    container.domain.wire(packages=['main.app.use_cases'])
    container.domain.risk_factor_dao.override(risk_factor_dao_mock)
    yield container
    container.unwire()


def run():
    pytest.main()


if __name__ == '__main__':
    run()
