from flask_restful import Resource, Api

DUMMY = {'success': True}


class BaseApi(Resource):
    endpoint = '/<string:id>'

    def get(self, **kwargs):
        """Receiving GET method request."""
        return DUMMY

    def post(self, **kwargs):
        """Receiving POST method request."""
        return DUMMY

    def put(self, **kwargs):
        """Receiving PUT method request."""
        return DUMMY

    def delete(self, **kwargs):
        """Receiving DELETE method request."""
        return DUMMY
