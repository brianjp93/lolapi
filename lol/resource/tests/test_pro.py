"""Testing file for resource.proplay
"""
import os
import sys
import pytest

from ...riot import Riot

KEY = os.environ.get('RIOT_API_KEY')
api = Riot(KEY)


def test_get_weekly_schedule():
    r = api.pro.get_weekly_schedule(102)
