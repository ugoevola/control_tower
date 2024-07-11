-- create database
CREATE DATABASE control_tower
    WITH
    OWNER = admin
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

-- create the tables
CREATE TABLE risk_factor_priority (
    organization_id UUID NOT NULL,
    project_id UUID NOT NULL,
    project_evaluation_id UUID NOT NULL,
    risk_factor_id UUID NOT NULL,
    risk_priority_score INTEGER,
    is_project_evaluation_last BOOLEAN,
    PRIMARY KEY (project_evaluation_id, risk_factor_id, risk_priority_score, is_project_evaluation_last)
);

CREATE TABLE risk_factor (
    id UUID PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    probability DECIMAL(3, 2) CHECK (probability >= 0 AND probability <= 1),
    impact TEXT
);

-- fill in the tables
INSERT INTO risk_factor (id, name, probability, impact)
VALUES
    ('9930919d-e316-4db7-a326-559289dc069b', 'Problèmes de financement', 0.6, 'modéré'),
    ('0442a458-4fc4-4f1f-a7a2-388a35023536', 'Retards dans la livraison de matériel', 0.8, 'élevé'),
    ('1710d973-074c-4c30-8d7b-f95bd06fa736', 'Changements dans les exigences du client', 0.7, 'variable'),
    ('f7f1207c-e120-4f9e-9103-8ad99c1ede61', 'Problèmes de ressources humaines', 0.5, 'modéré'),
    ('f0424b6c-e1c0-4299-9128-16f1081550e1', 'Problèmes techniques imprévus', 0.9, 'élevé');
