from uuid import UUID
from werkzeug.exceptions import BadRequest


class UuidValidator:

    @staticmethod
    def validate(value: str) -> None:
        try:
            UUID(value)
        except ValueError:
            raise BadRequest(description=f"{value} must be an uuid")
