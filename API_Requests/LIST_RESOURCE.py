from Utils.requestlink import *
import requests
import json
import jsonpath

def list_Resource():
    response = requests.get(get_ListResource)
    print(response.status_code)
    assert response.status_code == 200

    json_response = json.loads(response.text)
    print(json_response)

    pages = jsonpath.jsonpath(json_response, 'total_pages')
    print(pages[0])
