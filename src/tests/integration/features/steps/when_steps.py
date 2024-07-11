import requests

from behave import when

from main.app.common.enums import HttpMethod
from tests.integration.models import Context


@when('make a {http_method} request to {path} with')
def make_a_http_method_request_to_path_with(context: Context, http_method, path):
    http_method = HttpMethod[http_method]
    body = context.text

    context.headers['Content-type'] = 'application/json'
    response = requests.request(
        method=http_method.value,
        url=context.base_url + path,
        headers=context.headers,
        data=body
    )
    context.response = response


@when('make a {http_method} request to {path}')
def make_a_http_method_request_to_path(context: Context, http_method, path):
    http_method = HttpMethod[http_method]

    response = requests.request(
        method=http_method.value,
        url=context.base_url + path,
        headers=context.headers
    )
    context.response = response
