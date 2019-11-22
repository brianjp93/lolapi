"""Testing file for resource.thirdpartycode
"""
import os
from ...riot import Riot

KEY = os.environ.get('RIOT_API_KEY')
api = Riot(KEY)

def test_get():
    r = api.summoner.get(name='import antigrvty', region='na')
    data = r.json()
    r = api.thirdpartycode.get(data['id'], region='na')
    assert r.content == b''
