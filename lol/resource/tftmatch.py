import requests


REGION_CONVERSION = {
    'na': 'americas',
    'br': 'americas',
    'lan': 'americas',
    'las': 'americas',
    'oce': 'americas',
    'kr': 'asia',
    'jp': 'asia',
    'eune': 'europe',
    'euw': 'europe',
    'tr': 'europe',
    'ru': 'europe',
}


class TftMatch():

    def __init__(self, base):
        self.base = base
        self.version = 'v1'

    def get_base_url(self, region=None, general_region=None):
        if region is not None:
            if region in REGION_CONVERSION:
                selected_region = REGION_CONVERSION[region]
            else:
                raise Exception(f'region must be one of {REGION_CONVERSION.keys()}')
        elif general_region is not None:
            selected_region = general_region
        else:
            raise Exception('Must provide one of [region, general_region]')
        base_url = f'https://{selected_region}.api.riotgames.com/tft/match'
        return base_url

    def get(self, _id, region=None, general_region=None):
        base_url = self.get_base_url(region=region, general_region=general_region)
        url = f'{base_url}/{self.version}/matches/{_id}'
        return requests.get(url, headers=self.base.headers)

    def list_by_puuid(self, puuid, region=None, general_region=None):
        base_url = self.get_base_url(region=region, general_region=general_region)
        url = f'{base_url}/{self.version}/matches/by-puuid/{puuid}/ids'
        return requests.get(url, headers=self.base.headers)
