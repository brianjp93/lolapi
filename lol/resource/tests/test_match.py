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
        response = api.match.filter(data['puuid'], region='na')
        for x in response.json():
            match_ids.append(x)
    return match_ids


def test_get():
    match_ids = get_match_ids()
    response = api.match.get(match_ids[0], region='na')
    assert response.status_code == 200


def test_filter():
    r = api.summoner.get(name='importantigrvty', region='na')
    data = r.json()

    r = api.match.filter(data['puuid'], region='na')
    assert r.status_code == 200


def test_timeline():
    match_id = get_match_ids()[0]
    r = api.match.timeline(match_id, region='na')
    assert r.status_code == 200
