"""Test file for resource.tftleague.py
"""
import os
from ...riot import Riot

KEY = os.environ.get('RIOT_API_KEY')
api = Riot(KEY)

# These tests can't run until my api key has access to the tft endpoints
"""
def test_challenger():
    r = api.tftleague.challenger(region='na')
    assert r.status_code == 200

def test_by_summoner():
    r = api.summoner.get(name='importantigrvty', region='na')
    _id = r.json()['id']
    assert _id not in ['', None]
    r = api.tftleague.by_summoner(_id, region='na')
    assert r.status_code == 200
"""
