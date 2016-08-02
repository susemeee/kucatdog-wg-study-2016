import pytest
import requests

from app import mmap_reset
from run import DEFAULT_PORT


def build_request(method_name):
    method = getattr(requests, method_name, lambda: None)

    def send_request(endpoint='', data={}):
        response = method(
            'http://localhost:{}/{}'.format(DEFAULT_PORT, endpoint.lstrip('/')),
            data=data
        )
        return response

    return send_request


@pytest.fixture
def request_get(request):
    request.addfinalizer(mmap_reset)
    return build_request('get')


@pytest.fixture
def request_post(request):
    request.addfinalizer(mmap_reset)
    return build_request('post')


@pytest.fixture
def request_put(request):
    request.addfinalizer(mmap_reset)
    return build_request('put')


@pytest.fixture
def request_delete(request):
    request.addfinalizer(mmap_reset)
    return build_request('delete')
