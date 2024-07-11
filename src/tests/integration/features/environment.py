import time

from typing import Optional
from subprocess import Popen, PIPE

from tests.integration.models.context import Context

flask_process: Optional[Popen] = None
base_url = 'http://127.0.0.1:5000'


def before_scenario(context: Context, scenario):
    global flask_process
    context.base_url = base_url
    context.headers = {}
    global flask_process
    flask_process = Popen(['run-app'], stdout=PIPE, stderr=PIPE)
    time.sleep(2)


def after_scenario(context, scenario):
    global flask_process
    if flask_process:
        flask_process.terminate()
