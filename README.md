# Control Tower API

Control Tower API provides metrics on project's risk factors.

## Initialisation

Make sure to have a postgres SQL database running on your environment.
<br>
You can create and populate your database as-follow:
 - You will find, in `assets` folder, **SQL** script to create database and tables and fill them.
 - You can also fill the `risk_factor_priority` table with csv data in assets

Once done, change the database connection in the configuration file under `src/main/resources/config.yml`

## Lancement

### Linux

1 - dependencies installation ```pip install -e .```
<br>
2 - then run the app ```run-app```!

### Docker

build image
```commandline
docker build -t control_tower .
```

run it in docker container
```commandline
docker run -p 5000:5000 control_tower
```

## Tests

There are 2 types of tests :
- unit tests
- integration tests

> make sure to install dependencies before run tests
### Unit tests

Unit tests focus on business logic

```commandline
run-unit-tests
```

### Integration tests

Integration tests verify the behaviour of each exposed service 

```commandline
run-integration-tests
```


### Coverage

> TODO


# TODO
 - coverage
 - mocker les appels à la base de données pour les tests d'intégration
 - authentification
 - meilleure gestion des modules
 - gestion des variables d'environnement
 - gestion des handlers

# FIXES
 - lancement api en debug
 - docker image building