import requests
from datetime import datetime
from typing import Optional


class OverCountLimitError(Exception):
    pass


class InvalidQueueType(Exception):
    pass


class Match:
    """
    MATCH-V5
    https://developer.riotgames.com/api-methods/#match-v5
    """

    def __init__(self, base):
        self.base = base
        self.version = 'v5'

    def get(self, match_id, region=None):
        """Get a match by ID.

        Parameters
        ----------
        match_id : ID

        Returns
        -------
        JSON
            match data

        """
        base_url = self.base.get_base_url(region, use_v5_region=True)
        url = f'{base_url}/lol/match/{self.version}/matches/{match_id}'
        r = requests.get(url, headers=self.base.headers)
        return r

    def filter(
        self,
        puuid: str,
        region: Optional[str] = None,
        startTime: Optional[datetime] = None,
        endTime: Optional[datetime] = None,
        queue: Optional[int] = None,
        queueType: Optional[str] = None,
        start: Optional[int] = None,
        count: Optional[int] = None,
    ):
        """Get list of matches by account_id."""
        base_url = self.base.get_base_url(region, use_v5_region=True)
        params = {}
        if startTime:
            value = int(startTime.timestamp())
            params['startTime'] = value
        if endTime:
            value = int(endTime.timestamp())
            params['endTime'] = value
        if queue:
            params['queue'] = queue
        if queueType:
            if queueType not in ['ranked', 'normal', 'tourney', 'tutorial']:
                raise InvalidQueueType
            params['type'] = queueType
        if start:
            params['start'] = start
        if count:
            if count > 100:
                raise OverCountLimitError('Count must be <= 100.')
            params['count'] = count
        url = f'{base_url}/lol/match/{self.version}/matches/by-puuid/{puuid}/ids'
        r = requests.get(url, params=params, headers=self.base.headers)
        return r

    def timeline(self, match_id, region=None):
        """Get timeline data for a match.

        Parameters
        ----------
        match_id : ID
        region : str

        Returns
        -------
        JSON
            timeline data

        """
        base_url = self.base.get_base_url(region, use_v5_region=True)
        url = f'{base_url}/lol/match/{self.version}/matches/{match_id}/timeline'
        r = requests.get(url, headers=self.base.headers)
        return r
