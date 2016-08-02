import random

from . import (
    request_get, request_post, request_put, request_delete
)

cookie_flavors = ['strawberry', 'apple', 'mint', 'peach', 'zombie']


def new_cookie():
    return {
        'flavor': random.choice(cookie_flavors),
        'size': random.randint(10, 30),
    }


def test_cookie_client_get_empty_cookie_list(request_get):
    response = request_get('/cookie/')
    assert response.status_code == 200
    assert response.json() == []


def test_cookie_client_post_creation(request_post):
    cookie = new_cookie()
    response = request_post('/cookie/', data=cookie)
    assert response.status_code == 200
    data = response.json()
    assert 'id' in data

    return data['id'], cookie


def test_cookie_client_multiple_post_creation(request_post):
    id_list = []
    for i in range(10):
        cookie_id, _ = test_cookie_client_multiple_post_creation(request_post)
        assert cookie_id not in id_list
        id_list.append(cookie_id)

    response = request_get('/cookie/')
    assert response.status_code == 200
    assert len(response.json()) == 10

def test_cookie_client_created_cookie_has_length(request_get, request_post):
    test_cookie_client_post_creation(request_post)

    response = request_get('/cookie/')
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1


def test_cookie_client_created_cookie_is_accessable(request_get, request_post):
    cookie_id, cookie = test_cookie_client_post_creation(request_post)

    response = request_get('/cookie/{}'.format(cookie_id))
    assert response.status_code == 200
    data = response.json()
    assert data == cookie


def test_cookie_client_put_update(request_put, request_post):
    cookie_id, cookie = test_cookie_client_post_creation(request_post)
    new = new_cookie()
    response = request_put('/cookie/{}'.format(cookie_id), data=new)
    assert response.status_code == 200

    return cookie_id, new


def test_cookie_client_put_update_returns_updated_data(request_get, request_post, request_put):
    cookie_id, updated_cookie = test_cookie_client_put_update(request_put, request_post)

    response = request_get('/cookie/{}'.format(cookie_id))
    assert response.status_code == 200
    data = response.json()
    assert data == updated_cookie


def test_cookie_client_deletion(request_get, request_post, request_delete):
    cookie_id, cookie = test_cookie_client_post_creation(request_post)
    response = request_delete('/cookie/{}'.format(cookie_id))
    assert response.status_code == 200

    test_cookie_client_get_empty_cookie_list(request_get)
