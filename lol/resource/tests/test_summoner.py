"""Testing file for resource.summoner
"""
import os
import pytest

from ...riot import Riot

KEY = os.environ.get('RIOT_API_KEY')
api = Riot(KEY)


def test_get():
    r = api.summoner.get(name='importantigrvty', region='na')
    assert r.status_code == 200

    data = r.json()

    r = api.summoner.get(
        encrypted_account_id=data['accountId'],
        region='na'
    )
    assert r.status_code == 200

    r = api.summoner.get(encrypted_summoner_id=data['id'], region='na')
    assert r.status_code == 200

    r = api.summoner.get(encrypted_puuid=data['puuid'], region='na')
    assert r.status_code == 200

    with pytest.raises(Exception) as info:
        r = api.summoner.get(region='na')
    assert 'must be provided' in str(info.value)
