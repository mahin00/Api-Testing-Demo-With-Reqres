import requests
import json
import jsonpath
from Utils.requestlink import delete_delete

def del_user():
    response = requests.delete(delete_delete)
    print(response.status_code)
    assert response.status_code == 204