Feature: Get Risk Factor Resource Feature

  Scenario: get risk factor for a given id succeed
    When make a GET request to /risk_factor/9930919d-e316-4db7-a326-559289dc069b
    Then the response status code should be 200
    Then the response json body must be
    """json
    {
        "id": "9930919d-e316-4db7-a326-559289dc069b",
        "impact": "modéré",
        "name": "Problèmes de financement",
        "probability": "0.60"
    }
    """

  Scenario: get risk factor for a given id not found
    When make a GET request to /risk_factor/995fe37f-c629-4ff5-98af-f5afb82fcca2
    Then the response status code should be 404

  Scenario: get risk factor by passing a bad id
    When make a GET request to /risk_factor/f5afb82fcca2
    Then the response status code should be 400