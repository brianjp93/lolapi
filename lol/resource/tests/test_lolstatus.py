"""Testing file for resource.thirdpartycode
"""
import os
from ...riot import Riot

KEY = os.environ.get('RIOT_API_KEY')
api = Riot(KEY)

def test_get():
    r = api.lolstatus.get(region='na')
    assert r.status_code == 200
