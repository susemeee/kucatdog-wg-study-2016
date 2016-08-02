from app.api.base import BaseApi
from app.models import database


class CookieApi(BaseApi):
    endpoint = '/cookie/<string:cookie_name>'
    # Do what you want.
    pass
