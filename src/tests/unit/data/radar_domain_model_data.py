from uuid import UUID
from main.app.domain.models import RadarDomainModel


def get_radar_domain_model_list_ok():
    risk_factor_id_0 = UUID("b1ede577-bb8b-406d-a002-1912e450fd54")
    risk_factor_id_1 = UUID("c9a8ca2e-3e28-4903-8ca5-0cede76e3e3b")
    risk_factor_id_2 = UUID("5bcd64f5-a42f-4df6-8c33-7cabad98024e")
    radar_domain_model_0 = RadarDomainModel(
        risk_factor_name="Complétude du contrat",
        risk_factor_id=risk_factor_id_0,
        priority_score=0)
    radar_domain_model_1 = RadarDomainModel(
        risk_factor_name="Problèmes de financement",
        risk_factor_id=risk_factor_id_1,
        priority_score=1)
    radar_domain_model_2 = RadarDomainModel(
        risk_factor_name="Changements dans les exigences du client",
        risk_factor_id=risk_factor_id_2,
        priority_score=2)

    return [radar_domain_model_0, radar_domain_model_1, radar_domain_model_2]
