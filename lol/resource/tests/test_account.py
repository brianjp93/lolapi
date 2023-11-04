import os
from ...riot import Riot

KEY = os.environ.get('RIOT_API_KEY')
api = Riot(KEY)


def test_key():
    assert KEY not in ['', None]


def test_by_riot_id():
    r = api.account.by_riot_id("import antigrvty", "0grav")
    assert r.status_code == 200

