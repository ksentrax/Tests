import requests
import json

from requests.auth import HTTPBasicAuth


def test_create_with_list():
    url = "https://petstore.swagger.io/v2/user/createWithList"
    f = open("createWithListBody.json", "r")
    request_json = json.loads(f.read())
    response = requests.post(url, json=request_json)
    assert response.status_code == 200
    assert response.headers['Content-type'] == 'application/json'
    response_body = response.json()
    assert response_body["message"] == "ok"


def test_get_user():
    url = "https://petstore.swagger.io/v2/user/user1234"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.headers['accept'] == 'application/json'
    response_body = response.json()
    assert response_body["username"] == "user1234"


def test_update_user():
    url = "https://petstore.swagger.io/v2/user/user1234"
    f = open("updateUserBody.json", "r")
    request_json = json.loads(f.read())
    response = requests.put(url, json=request_json,
                            auth=HTTPBasicAuth('user1234', '00000000'))
    assert response.status_code == 200
    assert response.headers['Content-type'] == 'application/json'


def test_delete_user():
    url = "https://petstore.swagger.io/v2/user/user5678"
    response = requests.delete(url,
                               auth=HTTPBasicAuth('user5678', '11111111'))
    assert response.status_code == 200
    assert response.headers['accept'] == 'application/json'
    response_body = response.json()
    assert response_body["message"] == "user5678"


def test_login():
    url = "https://petstore.swagger.io/v2/user/login"
    payload = {"username": "user1234", "password": "00000000"}
    response = requests.get(url, params=payload)
    assert response.status_code == 200
    assert response.headers['accept'] == 'application/json'


def test_logout():
    url = "https://petstore.swagger.io/v2/user/logout"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.headers['accept'] == 'application/json'


def test_create_with_array():
    url = "https://petstore.swagger.io/v2/user/createWithArray"
    f = open("createWithArrayBody.json", "r")
    request_json = json.loads(f.read())
    response = requests.post(url, json=request_json)
    assert response.status_code == 200
    assert response.headers['Content-type'] == 'application/json'


def test_create_user():
    url = "https://petstore.swagger.io/v2/user"
    f = open("createUserBody.json", "r")
    request_json = json.loads(f.read())
    response = requests.post(url, json=request_json,
                             auth=HTTPBasicAuth('user1234', '00000000'))
    assert response.status_code == 200
    assert response.headers['Content-type'] == 'application/json'
