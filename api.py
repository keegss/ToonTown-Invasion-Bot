import sys
import requests
import time

# handle all requests to ttr api
class ttApi:
    def __init__(self):
        ttApi.url = 'https://www.toontownrewritten.com/api/'
        ttApi.headers = {
            'User-Agent': 'ToonTown Invasion Twitter Bot',
            'From': 'https://github.com/keegss'
        }

    def get_invasions(self):
        url = ttApi.url + 'invasions'
        return self.get_request(url)

    def get_request(self, url):
        try:
            r = requests.get(url, headers=ttApi.headers)
        except requests.exceptions.RequestException as e:
            print('ERROR: Unable to connect to ' + url)
            sys.exit(1)

        if r.status_code == 200:
            return r.json()
        else:
            print('ERROR: Bad Response: ' + str(r.status_code))
            sys.exit(1)

# return list of current invasions
def retrieve_invasions():
    api = ttApi()
    res = api.get_invasions()

    if res['error'] == None:
        return res['invasions']
    else:
        return {}
