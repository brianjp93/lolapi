"""Testing file for resource.league
"""
import os
from ...riot import Riot

KEY = os.environ.get('RIOT_API_KEY')
api = Riot(KEY)


def test_challenger():
    r = api.league.challenger('RANKED_SOLO_5x5', region='na')
    assert r.status_code == 200

def test_grandmaster():
    r = api.league.grandmaster('RANKED_SOLO_5x5', region='na')
    assert r.status_code == 200

def test_master():
    r = api.league.master('RANKED_SOLO_5x5', region='na')
    assert r.status_code == 200

def test_entries():
    r = api.summoner.get(name='importantigrvty', region='na')
    data = r.json()

    r = api.league.entries(data['id'], region='na')
    assert r.status_code == 200

def test_entries_list():
    r = api.league.entries_list('RANKED_SOLO_5x5', 'DIAMOND', 'I', region='na')
    assert r.status_code == 200
