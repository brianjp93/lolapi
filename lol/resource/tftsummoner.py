import requests


class TftSummoner():

    def __init__(self, base):
        self.base = base
        self.version = 'v1'

    def get(self, name=None, account_id=None, puuid=None, summoner_id=None, region=None):
        base_url = f'{self.base.base_url[region]}/tft/summoner'
        if name is not None:
            base_url = f'{base_url}/{self.version}/summoners/by-name/{name}'
        elif account_id is not None:
            base_url = f'{base_url}/{self.version}/summoners/by-account/{account_id}'
        elif puuid is not None:
            base_url = f'{base_url}/{self.version}/summoners/by-puuid/{puuid}'
        elif summoner_id is not None:
            base_url = f'{base_url}/{self.version}/summoners/{summoner_id}'
        else:
            raise Exception('Get method requires one of the kwargs [name, account_id, puuid, summoner_id].')
        return requests.get(base_url, headers=self.base.headers)
