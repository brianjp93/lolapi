import requests

class Account:
    """Account-V1
    - https://developer.riotgames.com/apis#account-v1/

    """

    def __init__(self, base):
        self.base = base

    def by_riot_id(self, game_name, tag_line, region='americas'):
        """Get list of Champion Rotations.
        """
        base_url = self.base.get_base_url(region, use_v5_region=True)
        url = '{}/riot/account/v1/accounts/by-riot-id/{}/{}'.format(base_url, game_name, tag_line)
        r = requests.get(url, headers=self.base.headers)
        return r

    def by_puuid(self, puuid, region='americas'):
        base_url = self.base.get_base_url(region, use_v5_region=True)
        url = '{}/riot/account/v1/accounts/by-puuid/{}'.format(base_url, puuid)
        r = requests.get(url, headers=self.base.headers)
        return r
