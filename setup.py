from setuptools import setup, find_packages

setup(
    name='control_tower',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        'flask~=3.0.3',
        'flask-restx~=1.3.0',
        'dependency_injector~=4.41.0',
        'pyyaml~=6.0.1',
        'werkzeug~=3.0.3',
        'flask-SQLAlchemy~=3.1.1',
        'SQLAlchemy~=2.0.31',
        'psycopg2-binary~=2.9.9',
        'pytest-flask~=1.3.0',
        'pytest~=8.2.2',
        'requests~=2.32.3',
        'behave~=1.2.6',
    ],
    entry_points={
        'console_scripts': [
            'run-app = main.app.main_app:run',
            'run-unit-tests = tests.unit.main_unit_test:run',
            'run-integration-tests = tests.integration.main_integration_test:run'
        ],
    },
)
