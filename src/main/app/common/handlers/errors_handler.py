from werkzeug.exceptions import HTTPException
from flask_restx import Api
from flask import json


def register_error_handlers(api: Api):

    @api.errorhandler(HTTPException)
    def handle_internal_error(e: HTTPException):
        response = e.get_response()
        response.data = json.dumps({
            "code": e.code,
            "name": e.name,
            "description": e.description,
        })
        response.content_type = "application/json"
        return response
