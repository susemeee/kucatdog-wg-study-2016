from app.api.base import BaseApi
from app.models.memory import MemoryBasedModel


class CookieApi(BaseApi):
    endpoint = '/cookie/<string:cookie_name>'
    # Do what you want.
    pass
