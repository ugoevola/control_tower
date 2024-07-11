from json import loads

from behave import then

from tests.integration.models import Context


@then('the response status code should be {status}')
def the_response_status_code_should_be(context: Context, status: str):
    received_status = context.response.status_code if context.response is not None else None
    assert int(status) == received_status, \
        f"Unexpected response status code, expected: {status}, received: {received_status}"


@then('the response json body must be')
def the_response_status_code_should_be(context: Context):
    received_body = context.response.json() if context.response else None
    assert loads(context.text) == received_body, \
        f"Unexpected response status body, expected: {context.text}, received: {received_body}"
