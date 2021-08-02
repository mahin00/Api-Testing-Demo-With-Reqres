import requests
import json
import jsonpath
from Utils.requestlink import *

def not_Found():
    response = requests.get(get_SingleUsernotfound)
    print(response.status_code)
    assert response.status_code == 404

    json_response = json.loads(response.text)
    print(json_response)
    assert len(json_response) == 0
