import requests

from settings import AUTH, SERVER, PORT

def make_request(path):
    if AUTH:
        r = requests.get('http://%s:%s%s' %(SERVER, PORT, path),
                         auth=AUTH)
    else:
        r = requests.get('http://%s:%s%s' %(SERVER, PORT, path))
    if r.status_code != 200:
        return False
    return r.text