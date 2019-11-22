"""Testing file for resource.lolstaticdata
"""
import os
from ...riot import Riot

KEY = os.environ.get('RIOT_API_KEY')
api = Riot(KEY)

VERSION = '9.22.1'

def test_champions():
    r = api.lolstaticdata.champions(version=VERSION)
    assert r.status_code == 200

def test_items():
    pass

def test_languages():
    pass

def test_masteries():
    pass

def test_profile_icons():
    pass

def test_realms():
    pass

def test_runes():
    pass

def test_runes_reforged():
    pass

def test_summoner_spells():
    pass

def test_versions():
    pass
