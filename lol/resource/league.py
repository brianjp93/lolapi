import requests
import logging

LOGGER = logging.getLogger(__name__)


class League:
    """
    LEAGUE-V4
    https://developer.riotgames.com/api-methods/#league-v4
    """

    def __init__(self, base):
        self.base = base
        self.version = 'v4'

    def challenger(self, queue, region=None):
        """Get the challenger league for a given queue

        Parameters
        ----------
        queue : str
            enum(
                RANKED_SOLO_5x5,
                RANKED_FLEX_SR,
                RANKED_FLEX_TT
            )
        region : str

        Returns
        -------
        JSON

        """
        base_url = self.base.base_url[region]
        url = f'{base_url}/lol/league/{self.version}/challengerleagues/by-queue/{queue}'
        r = requests.get(url, headers=self.base.headers)
        return r

    def grandmaster(self, queue, region=None):
        """Get the GrandMaster league for a given queue.

        Parameters
        ----------
        queue : str
            enum(
                RANKED_SOLO_5x5,
                RANKED_FLEX_SR,
                RANKED_FLEX_TT
            )
        region : str

        Returns
        -------
        JSON Response

        """
        base_url = self.base.base_url[region]
        url = f'{base_url}/lol/league/{self.version}/grandmasterleagues/by-queue/{queue}'
        r = requests.get(url, headers=self.base.headers)
        return r

    def master(self, queue, region=None):
        """Get the Master league for a given queue.

        Parameters
        ----------
        queue : str
            enum(
                RANKED_SOLO_5x5,
                RANKED_FLEX_SR,
                RANKED_FLEX_TT
            )
        region : str

        Returns
        -------
        JSON Response

        """
        base_url = self.base.base_url[region]
        url = f'{base_url}/lol/league/{self.version}/masterleagues/by-queue/{queue}'
        r = requests.get(url, headers=self.base.headers)
        return r

    def league(self, league_id, region=None):
        """Get league by ID

        Parameters
        ----------
        league_id : ID
        region : str

        Returns
        -------
        JSON Response

        """
        base_url = self.base.base_url[region]
        url = f'{base_url}/lol/league/{self.version}/leagues/{league_id}/'
        r = requests.get(url, headers=self.base.headers)
        return r

    def entries(self, encrypted_summoner_id, region=None):
        """Get rank entries by encrypted_summoner_id.

        Parameters
        ----------
        encrypted_summoner_id : ID
        region : str

        Returns
        -------
        JSON Response

        """
        base_url = self.base.base_url[region]
        url = f'{base_url}/lol/league/{self.version}/entries/by-summoner/{encrypted_summoner_id}'
        r = requests.get(url, headers=self.base.headers)
        return r

    def entries_list(self, queue, tier, division, page=1, region=None):
        """Get a page of rank entries in a queue, tier, division.

        Parameters
        ----------
        queue : str
        tier : str
        division : str
        page : int
        region : str

        Returns
        -------

        """
        params = {'page': page}
        base_url = self.base.base_url[region]
        url = f'{base_url}/lol/league/{self.version}/entries/{queue}/{tier}/{division}'
        r = requests.get(url, params=params, headers=self.base.headers)
        return r
