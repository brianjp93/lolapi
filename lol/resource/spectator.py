import requests


class Spectator:
    """
    SPECTATOR-V5
    https://developer.riotgames.com/apis#spectator-v5
    """

    def __init__(self, base):
        self.base = base
        self.version = 'v5'

    def get(self, puuid, region=None):
        base_url = self.base.get_base_url(region, use_v5_region=False)
        url = f'{base_url}/lol/spectator/{self.version}/active-games/by-summoner/{puuid}'
        r = requests.get(url, headers=self.base.headers)
        return r

    def featured(self, region=None):
        base_url = self.base.get_base_url(region, use_v5_region=False)
        url = f'{base_url}/lol/spectator/{self.version}/featured-games'
        r = requests.get(url, headers=self.base.headers)
        return r
