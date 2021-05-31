import requests
import json

from requests.auth import HTTPBasicAuth


def test_create_with_list():
    url = "https://petstore.swagger.io/v2/user/createWithList"
    f = open("createWithListBody.json", "r")
    request_json = json.loads(f.read())
    response = requests.post(url, json=request_json)
    assert response.status_code == 200
    return response.json()


def test_get_user():
    url = "https://petstore.swagger.io/v2/user/user1234"
    response = requests.get(url)
    assert (response.status_code == 200), "Status code is not 200."
    response_body = response.json()
    assert response_body["username"] == "user1234"
    return response.json()


def test_update_user():
    url = "https://petstore.swagger.io/v2/user/user1"
    f = open("updateUserBody.json", "r")
    request_json = json.loads(f.read())
    response = requests.put(url, json=request_json,
                            auth=HTTPBasicAuth('user1234', '00000000'))
    assert response.status_code == 200
    return response.json()


def test_delete_user():
    url = "https://petstore.swagger.io/v2/user/user5678"
    response = requests.delete(url,
                               auth=HTTPBasicAuth('user5678', '11111111'))
    assert response.status_code == 200
    return response.json()


def test_login():
    url = "https://petstore.swagger.io/v2/user/login"
    payload = {"username": "user1234", "password": "00000000"}
    response = requests.get(url, params=payload)
    return response.json()


def test_logout():
    url = "https://petstore.swagger.io/v2/user/logout"
    response = requests.get(url)
    assert response.status_code == 200
    return response.json()


def test_create_with_array():
    url = "https://petstore.swagger.io/v2/user/createWithArray"
    f = open("createWithArrayBody.json", "r")
    request_json = json.loads(f.read())
    response = requests.post(url, json=request_json)
    assert response.status_code == 200
    return response.json()


def test_create_user():
    url = "https://petstore.swagger.io/v2/user"
    f = open("createUserBody.json", "r")
    request_json = json.loads(f.read())
    response = requests.post(url, json=request_json,
                             auth=HTTPBasicAuth('user1234', '00000000'))
    assert response.status_code == 200
    assert response.headers['Content-type'] == 'application/json'
    return response.json()


if __name__ == "__main__":
    print(test_create_with_list())
    print(test_get_user())
    print(test_update_user())
    print(test_delete_user())
    print(test_login())
    print(test_logout())
    print(test_create_with_array())
    print(test_create_user())
