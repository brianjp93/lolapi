import requests


class TftLeague():

    def __init__(self, base):
        self.base = base
        self.version = 'v1'

    def challenger(self, region=None):
        base_url = f'{self.base.base_url[region]}/tft/league/{self.version}/challenger'
        return requests.get(base_url, headers=self.base.headers)

    def by_summoner(self, encrypted_summoner_id, region=None):
        base_url = f'{self.base.base_url[region]}/tft/league/{self.version}/entries/by-summoner/{encrypted_summoner_id}'
        return requests.get(base_url, headers=self.base.headers)

    def entries(self, tier, division, region=None):
        """

        Parameters
        ----------
        tier : str
            enum[IRON, BRONZE, SILVER, GOLD, PLATINUM, DIAMOND]
        division : str
            enum[I, II, III, IV]
        region : str

        Returns
        -------
        list

        """
        base_url = f'{self.base.base_url[region]}/tft/league/{self.version}/entries/{tier}/{division}'
        return requests.get(base_url, headers=self.base.headers)

    def grandmaster(self, region=None):
        base_url = f'{self.base.base_url[region]}/tft/league/{self.version}/grandmaster'
        return requests.get(base_url, headers=self.base.headers)

    def league(self, league_id, region=None):
        base_url = f'{self.base.base_url[region]}/tft/league/{self.version}/leagues/{league_id}'
        return requests.get(base_url, headers=self.base.headers)

    def master(self, region=None):
        base_url = f'{self.base.base_url[region]}/tft/league/{self.version}/master'
        return requests.get(base_url, headers=self.base.headers)
