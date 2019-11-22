"""Testing file for resource.spectator
"""
import os
from ...riot import Riot

KEY = os.environ.get('RIOT_API_KEY')
api = Riot(KEY)

def test_get():
    r = api.spectator.featured(region='na')
    data = r.json()
    name = data['gameList'][0]['participants'][0]['summonerName']
    
    r = api.summoner.get(name=name, region='na')
    data = r.json()
    r = api.spectator.get(data['id'], region='na')
    assert r.status_code == 200

def test_featured():
    r = api.spectator.featured(region='na')
    assert r.status_code == 200
