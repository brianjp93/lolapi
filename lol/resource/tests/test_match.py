"""Testing file for resource.match
"""
import os
from ...riot import Riot

KEY = os.environ.get('RIOT_API_KEY')
api = Riot(KEY)

match_ids = []

def get_match_ids():
    global match_ids
    if match_ids:
        pass
    else:
        r = api.summoner.get(name='importantigrvty', region='na')
        data = r.json()

        r = api.match.filter(data['accountId'], region='na')
        for x in r.json()['matches']:
            match_ids.append(x['gameId'])
    return match_ids

def test_get():
    match_ids = get_match_ids()
    r = api.match.get(match_ids[0], region='na')
    assert r.status_code == 200

def test_filter():
    r = api.summoner.get(name='importantigrvty', region='na')
    data = r.json()

    r = api.match.filter(data['accountId'], region='na')
    assert r.status_code == 200

def test_timeline():
    match_id = get_match_ids()[0]
    r = api.match.timeline(match_id, region='na')
    assert r.status_code == 200

def test_tournament_all():
    pass
