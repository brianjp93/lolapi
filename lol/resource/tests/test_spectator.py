"""Testing file for resource.spectator
"""
import os
from ...riot import Riot

KEY = os.environ.get('RIOT_API_KEY')
api = Riot(KEY)

def test_get():
    r = api.spectator.featured(region='na')
    data = r.json()
    puuid = data['gameList'][0]['participants'][0]['puuid']
    
    r = api.spectator.get(puuid, region='na')
    assert r.status_code == 200

def test_featured():
    r = api.spectator.featured(region='na')
    assert r.status_code == 200
