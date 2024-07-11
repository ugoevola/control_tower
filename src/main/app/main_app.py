from main.app import app, api, config, db_client

from .app_container import AppContainer

container = AppContainer()
container.config.from_dict(config)
container.db_client.override(db_client)
container.api.override(api)
container.clients.wire(packages=['main.app.domain.dao'])
container.domain.wire(packages=['main.app.use_cases'])
container.use_cases.wire(packages=['main.app.web'])


def run():
    app.run(debug=config.get('flask').get('debug'), port=config.get('flask').get('port'))


if __name__ == '__main__':
    run()
