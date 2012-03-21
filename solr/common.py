import sys

import requests

from settings import AUTH, SERVER, PORT

def make_request(path):
    try:
        if AUTH:
            r = requests.get('http://%s:%s%s' %(SERVER, PORT, path),
                             auth=AUTH)
        else:
            r = requests.get('http://%s:%s%s' %(SERVER, PORT, path))
    except Exception, e:
        print e
        sys.exit(-1)
    if r.status_code != 200:
        return None
    return r.text