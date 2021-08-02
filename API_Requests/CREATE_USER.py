import requests
import json
import jsonpath
from Utils.requestlink import post_Create
from Utils.jsonData import createUser
import allure

@allure.step("varify create user")
def create_user():
    response = requests.post(post_Create, createUser)
    status_code = response.status_code
    assert response.status_code == 201
    print(response.headers.get('Content-Length'))
    res_json = json.loads(response.text)
    assert res_json != []
    print(res_json)
    id = jsonpath.jsonpath(res_json, 'id')
    assert id != False
    print(id[0])
    name = jsonpath.jsonpath(res_json, 'name')
    print(name[0])
    assert name[0] == "morpheus"


create_user()