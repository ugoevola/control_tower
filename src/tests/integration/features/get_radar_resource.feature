Feature: Get Radar Resource Feature

  Scenario: get radar for a given organisation succeed
    When make a GET request to /organisation/1c7cadcc-064f-4a66-8d38-f4828c0253b0/radar
    Then the response status code should be 200
    Then the response json body must be
    """json
    [
        {
            "priority_score": 1,
            "risk_factor_id": "1710d973-074c-4c30-8d7b-f95bd06fa736",
            "risk_factor_name": "Changements dans les exigences du client"
        },
        {
            "priority_score": 2,
            "risk_factor_id": "0442a458-4fc4-4f1f-a7a2-388a35023536",
            "risk_factor_name": "Retards dans la livraison de matériel"
        },
        {
            "priority_score": 3,
            "risk_factor_id": "f0424b6c-e1c0-4299-9128-16f1081550e1",
            "risk_factor_name": "Problèmes techniques imprévus"
        },
        {
            "priority_score": 3,
            "risk_factor_id": "9930919d-e316-4db7-a326-559289dc069b",
            "risk_factor_name": "Problèmes de financement"
        },
        {
            "priority_score": 5,
            "risk_factor_id": "f7f1207c-e120-4f9e-9103-8ad99c1ede61",
            "risk_factor_name": "Problèmes de ressources humaines"
        }
    ]
    """

  Scenario: get radar for a given non-existent organisation
    When make a GET request to /organisation/995fe37f-c629-4ff5-98af-f5afb82fcca2/radar
    Then the response status code should be 404

  Scenario: get radar by passing a bad id
    When make a GET request to /organisation/f5afb82fcca2/radar
    Then the response status code should be 400
