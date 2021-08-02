import requests
import json
import jsonpath
from Utils.requestlink import get_delayedResponse

def delayed_response():
    time = 5
    response = requests.get(get_delayedResponse, timeout=time)
    status = response.status_code
    print(status)
    print(response.elapsed)
    if time > 3:
        assert status == 200
    body = json.loads(response.text)
    assert body != []
delayed_response()