import requests
import json
import jsonpath
from Utils.requestlink import *

def single_resource_found():
    response = requests.get(get_SingleResource)
    status = response.status_code
    print(status)
    assert status == 200

    json_response = json.loads(response.text)
    print(json_response)

    body = json.loads(response.content)
    assert body != 0
    name = jsonpath.jsonpath(json_response, "data.name")
    print(name)