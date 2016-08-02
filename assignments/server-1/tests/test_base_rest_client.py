from . import (
    request_get, request_post, request_put, request_delete
)


def test_base_rest_client_get(request_get):
    response = request_get('1')
    assert response.status_code == 200


def test_base_rest_client_post(request_post):
    response = request_post('1')
    assert response.status_code == 200


def test_base_rest_client_put(request_put):
    response = request_put('1')
    assert response.status_code == 200


def test_base_rest_client_delete(request_delete):
    response = request_delete('1')
    assert response.status_code == 200
