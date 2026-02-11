import pytest
from api_framework import client

def test_get_request():
    response = client.send_get_request("/posts/1")
    print(response.status_code)
    assert response.status_code == 200

def test_post_request():
    data = {'userid': '8989', 'title': 'anca', 'body': 'test'}
    response = client.send_post_request("/posts", data)
    receive_response = response.json()
    assert response.status_code == 201
    assert receive_response['body'] == 'test'

def test_delete():
    deleted_resource = '/posts/1'
    response = client.send_delete_request(deleted_resource)
    assert response.status_code == 200


@pytest.mark.parametrize("bad_endpoints",
                         ["/posts/9999",
                          "posts/_12",
                          "posts/&",
                          "posts/1&",
                          "posts/1<2"])
def test_invalid_endpoints(bad_endpoints):
    response = client.send_get_request(bad_endpoints)
    assert response.status_code == 404

@pytest.mark.parametrize("corrupted_data",
                         [{'title': 'anca', 'body': 'test'},
                          {'userid': '8989', 'body': 'test'},
                          {'userid': '8989', 'title': 'anca', },
                          {'userids': '8989', 'title': 'anca', 'body': 'test'},
                          {},
                          {'userids': 8989, 'title': 123, 'body': 2.0}]
                         )
def test_post_corrupted_data(corrupted_data):
    response = client.send_post_request("/posts", corrupted_data)
    # JSONPlaceholder accepts any data and returns 201
    # A real API would return 400 (Bad Request) for invalid data
    assert response.status_code == 201

def test_delete_nonexistent():
    response = client.send_delete_request("/posts/9999")
    # JSONPlaceholder returns 200 even for non-existent resources
    # A real API would return 404 (Not Found)
    assert response.status_code == 200
