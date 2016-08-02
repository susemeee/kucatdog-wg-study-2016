from . import (
    request_get, request_post, request_put, request_delete
)

def test_cookie_client_get_empty_returns_404(request_get):
    response = request_get('/cookie/999')
    assert response.status_code == 404


def test_cookie_client_put_empty_returns_404(request_put):
    response = request_put('/cookie/999')
    assert response.status_code == 404


def test_cookie_client_delete_empty_returns_404(request_delete):
    response = request_delete('/cookie/999')
    assert response.status_code == 404


def test_cookie_client_get_malformed_data_returns_400(request_get):
    response = request_get('/cookie/999', data='{')
    assert response.status_code == 400


def test_cookie_client_post_malformed_data_returns_400(request_post):
    response = request_post('/cookie/999', data='{')
    assert response.status_code == 400


def test_cookie_client_put_malformed_data_returns_400(request_put):
    response = request_put('/cookie/999', data='{')
    assert response.status_code == 400


def test_cookie_client_delete_malformed_data_returns_400(request_delete):
    response = request_delete('/cookie/999', data='{')
    assert response.status_code == 400
