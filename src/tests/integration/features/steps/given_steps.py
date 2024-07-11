from behave import given

from tests.integration.models import Context


@given('authorization')
def authorization(context: Context):
    authorization_token = 'your_generated_token'
    context.headers['authorization'] = authorization_token
