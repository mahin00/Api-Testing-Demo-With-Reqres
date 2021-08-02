import requests
import json
import jsonpath
from Utils.requestlink import *
from Utils.jsonData import *




#Read input json file
# request_json = json.loads(createUser)
# print(createUser)

def post_register_unsuccessfull():
    response = requests.post(post_RegisterUnuccessful, post_login_unsuccessfull)
    status_code = response.status_code
    print(status_code)
    assert status_code == 400

    res_json = json.loads(response.text)
    print(res_json)

    email = jsonpath.jsonpath(res_json, 'email')
    print(email)
    password = jsonpath.jsonpath(res_json, 'password')
    print(password)
    assert password == 0
    error = jsonpath.jsonpath(res_json, 'error')
    print(error[0])

post_register_unsuccessfull()