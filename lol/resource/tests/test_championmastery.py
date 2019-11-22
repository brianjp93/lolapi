"""Testing file for resource.championmastery
"""
import os
from ...riot import Riot

KEY = os.environ.get('RIOT_API_KEY')
api = Riot(KEY)

SUMMONER = {}

def get_summoner():
    global SUMMONER
    if SUMMONER:
        pass
    else:
        r = api.summoner.get(name='import antigrvty', region='na')
        data = r.json()
        SUMMONER = data
    return SUMMONER

def test_all():
    summoner = get_summoner()
    r = api.championmastery.all(summoner['id'], region='na')
    assert r.status_code == 200

def test_get():
    summoner = get_summoner()
    r = api.championmastery.get(summoner['id'], 1, region='na')
    assert r.status_code == 200

def test_total():
    summoner = get_summoner()
    r = api.championmastery.total(summoner['id'], region='na')
