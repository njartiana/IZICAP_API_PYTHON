from json import dumps

import pytest
import requests
from config import *


@pytest.fixture(scope='module')
def generate_token():
    print("-----------SETUP-------------")
    _url = BaseUrl + "/tokens"
    body = dumps({
        'username': 'admin',
        'password': 'admin'
    })
    headers = {
        'Content-type': 'application/json'
    }
    generate_token = requests.post(url=_url, data=body, headers=headers)
    if generate_token.status_code == 201:
        print("\nToken created successful")
        return generate_token
    if generate_token.status_code == 200:
        print("\nToken refresh successful")
        return generate_token


@pytest.fixture
def create_dynamic_user(generate_token):
    response = generate_token.json()
    _url = BaseUrl + "/users"
    body = dumps({
        "username": username,
        "password": password
    })
    headers = {
        'Content-type': 'application/json',
        'Authorization': 'Bearer ' + response['token']
    }
    create_dynamic_user = requests.post(url=_url, data=body, headers=headers)
    if create_dynamic_user.status_code == 201:
        return create_dynamic_user


@pytest.fixture
def create_static_user(generate_token):
    response = generate_token.json()
    _url = BaseUrl + "/users"
    body = dumps({
        "username": 'username11',
        "password": 'password11'
    })
    headers = {
        'Content-type': 'application/json',
        'Authorization': 'Bearer ' + response['token']
    }
    create_static_user = requests.post(url=_url, data=body, headers=headers)
    if create_static_user.status_code == 201:
        return create_static_user
    if create_static_user.status_code == 409:
        return create_static_user

@pytest.fixture
def generate_user_token():
    print("-----------SETUP-------------")
    _url = BaseUrl + "/tokens"
    body = dumps({
        'username': 'username11',
        'password': 'password11'
    })
    headers = {
        'Content-type': 'application/json'
    }
    generate_user_token = requests.post(url=_url, data=body, headers=headers)
    if generate_user_token.status_code == 201:
        return generate_user_token
    if generate_user_token.status_code == 200:
        print("\nToken refresh successful")
        return generate_user_token

@pytest.fixture
def create_user_by_user(generate_user_token):
    response = generate_user_token.json()
    _url = BaseUrl + "/users"
    body = dumps({
        "username": username,
        "password": password
    })
    headers = {
        'Content-type': 'application/json',
        'Authorization': 'Bearer ' + response['token']
    }
    create_user_by_user = requests.post(url=_url, data=body, headers=headers)
    if create_user_by_user.status_code == 403:
        return create_user_by_user


@pytest.fixture
def create_user_by_unexisting_token():
    _url = BaseUrl + "/users"
    body = dumps({
        "username": username,
        "password": password
    })
    headers = {
        'Content-type': 'application/json',
        'Authorization': 'Bearer 13qzfdd5qsdfsqd5qdf5qez5ffqe8q84hdjty'
    }
    create_user_by_unexisting_token = requests.post(url=_url, data=body, headers=headers)
    if create_user_by_unexisting_token.status_code == 401:
        return create_user_by_unexisting_token