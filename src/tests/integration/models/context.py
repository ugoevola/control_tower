from requests import Response
from typing import Optional


class Context:
    base_url: Optional[str]
    headers: Optional[dict]
    response: Optional[Response]
    text: Optional[str]
