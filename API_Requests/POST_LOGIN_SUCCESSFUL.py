import requests
import json
import jsonpath
from Utils.requestlink import *
from Utils.jsonData import *




#Read input json file
# request_json = json.loads(createUser)
# print(createUser)
def login_pass():
    response = requests.post(post_RegisterSuccessful, post_reg_body)
    status_code = response.status_code
    print(status_code)
    assert status_code == 200

    res_json = json.loads(response.text)
    print(res_json)

    id = jsonpath.jsonpath(res_json, 'id')
    print(id[0])
    assert len(id) != 0