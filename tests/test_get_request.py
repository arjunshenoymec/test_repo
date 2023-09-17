from http import HTTPStatus

import pytest
import requests


def test_response_from_get_request():
    url = "https://jsonplaceholder.typicode.com/posts/10"

    response = requests.get(url)

    assert response.status_code == HTTPStatus.OK

    response_body = response.json()

    assert 'id' in response_body
    assert 'userId' in response_body
    assert 'title' in response_body
    assert type(response_body['title']) == str


def test_request_to_random_uri_fails():
    url = "https://jsonplaceholder.typicode.com/random"

    response =  requests.get(url)

    assert response.status_code == HTTPStatus.NOT_FOUND
