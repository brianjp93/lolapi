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

def test_get_single_champion():
    r = api.lolstaticdata.champions(name='Tristana', version=VERSION)
    assert r.status_code == 200

def test_items():
    r = api.lolstaticdata.items(version=VERSION)
    assert r.status_code == 200

def test_languages():
    r = api.lolstaticdata.languages()
    assert r.status_code == 200

def test_profile_icons():
    r = api.lolstaticdata.profile_icons(version=VERSION)
    assert r.status_code == 200

def test_realms():
    r = api.lolstaticdata.realms(region='na')
    assert r.status_code == 200

def test_runes_reforged():
    r = api.lolstaticdata.runes_reforged(version=VERSION)
    assert r.status_code == 200

def test_summoner_spells():
    r = api.lolstaticdata.summoner_spells(version=VERSION)
    assert r.status_code == 200

def test_versions():
    r = api.lolstaticdata.versions()
    assert r.status_code == 200
