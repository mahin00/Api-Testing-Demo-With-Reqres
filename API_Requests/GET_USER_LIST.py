import requests
import json
import jsonpath
from Utils.requestlink import *

def get_List_Users():
    response = requests.get(get_AllUsers)
    print(response.status_code)
    assert response.status_code == 200

    json_response = json.loads(response.text)
    print(json_response)

    pages = jsonpath.jsonpath(json_response, 'total_pages')
    print(pages[0])

    # assert
    assert pages[0] == 2