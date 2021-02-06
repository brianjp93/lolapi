import requests


class Pro:
    host_1 = 'http://{}.lolesports.com'

    def __init__(self, base):
        self.base = base
        self.region = 'na'

    def get_weekly_schedule(self, tournament: int, expand_matches=1, region=None):
        """

        Parameters
        ----------
        tournament: int
        expand_matches: 1 or 0
        region: str

        Returns
        -------
        json

        """
        region = region if region else self.region
        url = self.host_1.format(region)
        url = f'{url}/api/programming.json'
        params = {
            'method': 'all',
            'expand_matches': expand_matches,
            'tournament': tournament,
        }
        params = {f'parameters[{key}]': val for key, val in params.items()}
        r = requests.get(url, params=params)
        return r
