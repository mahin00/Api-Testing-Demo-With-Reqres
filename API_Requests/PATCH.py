import requests
import json
import jsonpath
from Utils.requestlink import pathch_update
from Utils.jsonData import patchUser

def patch():
    patch_response = requests.patch(pathch_update, patchUser)
    status = patch_response.status_code
    print(status)
    assert status == 200

    res_json = json.loads(patch_response.text)
    print(res_json)
    update = jsonpath.jsonpath(res_json, 'name')
    print("Fatch name from API: " + update[0])
    assert update[0] == "Shashwata"
