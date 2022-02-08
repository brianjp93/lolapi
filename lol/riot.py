import sys
import os

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(
    os.path.realpath(
        os.path.join(
            os.getcwd(),
            os.path.expanduser(__file__)
        )
    )
)
package_path = os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT))
sys.path.append(package_path)

from lol import resource


class RiotBase:

    base_url = {
        'br': 'https://br1.api.riotgames.com',
        'br1': 'https://br1.api.riotgames.com',

        'eune': 'https://eun1.api.riotgames.com',
        'eun': 'https://eun1.api.riotgames.com',
        'eun1': 'https://eun1.api.riotgames.com',

        'euw': 'https://euw1.api.riotgames.com',
        'euw1': 'https://euw1.api.riotgames.com',

        'jp': 'https://jp1.api.riotgames.com',
        'jp1': 'https://jp1.api.riotgames.com',

        'kr': 'https://kr.api.riotgames.com',
        'kr1': 'https://kr.api.riotgames.com',

        'lan': 'https://la1.api.riotgames.com',
        'la1': 'https://la1.api.riotgames.com',

        'las': 'https://la2.api.riotgames.com',
        'la2': 'https://la2.api.riotgames.com',

        'na': 'https://na1.api.riotgames.com',
        'na1': 'https://na1.api.riotgames.com',

        'oce': 'https://oc1.api.riotgames.com',
        'oc1': 'https://oc1.api.riotgames.com',

        'tr': 'https://tr1.api.riotgames.com',
        'tr1': 'https://tr1.api.riotgames.com',

        'ru': 'https://ru.api.riotgames.com',

        'pbe': 'https://pbe1.api.riotgames.com',
        'pbe1': 'https://pbe1.api.riotgames.com',

        'americas': 'https://americas.api.riotgames.com',
        'europe': 'https://europe.api.riotgames.com',
        'asia': 'https://asia.api.riotgames.com',
    }

    routes = {
        'americas': {'na', 'na1', 'br', 'br1', 'lan', 'la1', 'las', 'la2', 'oce', 'oc1'},
        'europe': {'eune', 'eun', 'eun1', 'euw', 'euw1', 'tr', 'tr1', 'ru'},
        'asia': {'kr', 'kr1', 'jp', 'jp1'},
    }

    def __init__(self, key):
        self.key = key
        self.headers = self.get_headers()

    def get_headers(self):
        headers = {
            "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Riot-Token": self.key,
            "Accept-Language": "en-US,en;q=0.8",
        }
        return headers

    def get_base_url(self, region: str, use_v5_region=False):
        if use_v5_region:
            for new_region, val in self.routes.items():
                if region in val:
                    return self.base_url[new_region]
        return self.base_url[region]


class Riot:
    def __init__(self, key):
        self.key = key
        self.base = RiotBase(key)

        self.champion = resource.Champion(self.base)
        self.championmastery = resource.ChampionMastery(self.base)
        self.league = resource.League(self.base)
        self.lolstaticdata = resource.LolStaticData(self.base)
        self.lolstatus = resource.LolStatus(self.base)
        self.masteries = resource.Masteries(self.base)
        self.match = resource.Match(self.base)
        self.spectator = resource.Spectator(self.base)
        self.summoner = resource.Summoner(self.base)
        self.thirdpartycode = resource.ThirdPartyCode(self.base)
        self.tftleague = resource.TftLeague(self.base)
        self.tftmatch = resource.TftMatch(self.base)
        self.tftsummoner = resource.TftSummoner(self.base)
        self.pro = resource.Pro(self.base)
