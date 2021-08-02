import requests
import json
import jsonpath
from Utils.requestlink import *

def get_User():
    response = requests.get(get_SingleUser)
    print(response.status_code)
    assert response.status_code == 200

    # parse response to json format
    json_response = json.loads(response.text)
    print(json_response)

    # fetch value using json_path
    id = jsonpath.jsonpath(json_response, "data.id")
    print(id)
    assert id[0] == 2
