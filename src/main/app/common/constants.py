from sqlalchemy import text

GET_AVERAGE_PRIORITY_SCORES_REQUEST = text("""
    SELECT 
        rfp.risk_factor_id AS risk_factor_id,
        rf.name AS risk_factor_name,
        RANK() OVER (ORDER BY AVG(rfp.risk_priority_score)) AS priority_score
    FROM 
        risk_factor_priority rfp
    JOIN 
        risk_factor rf 
        ON rfp.risk_factor_id = rf.id
    WHERE 
        rfp.organization_id = :organization_id 
        AND rfp.is_project_evaluation_last = TRUE
    GROUP BY 
        rfp.risk_factor_id, 
        rf.name
    ORDER BY 
        AVG(rfp.risk_priority_score);
""")
