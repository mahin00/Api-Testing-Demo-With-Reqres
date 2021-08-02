import requests
import json
import jsonpath
from Utils.requestlink import *

def single_Resource_Not_Found():
    response = requests.get(get_SingleResourceNotfound)
    print(response.status_code)
    assert response.status_code == 404

    json_response = json.loads(response.text)
    print(json_response)
    assert len(json_response) == 0