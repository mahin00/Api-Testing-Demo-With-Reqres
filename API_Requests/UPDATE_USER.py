import requests
import json
import jsonpath
from Utils.requestlink import *
from Utils.jsonData import *

def get_Update_User():
    response = requests.put(put_update, createUser)
    status_code = response.status_code
    assert response.status_code == 200
    # print(response.headers.get('Content-Length'))
    res_json = json.loads(response.text)
    print(res_json)
    update = jsonpath.jsonpath(res_json, 'updatedAt')
    print("Fatch updateAt from API: " + update[0])