"""Testing file for resource.champion
"""
import os
from ...riot import Riot

KEY = os.environ.get('RIOT_API_KEY')
api = Riot(KEY)

def test_key():
    assert KEY not in ['', None]

def test_rotations():
    r = api.champion.rotations(region='na')
    assert r.status_code == 200
