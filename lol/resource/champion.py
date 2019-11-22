import requests

class Champion:
    """
    CHAMPION-V3
    https://developer.riotgames.com/api-methods/#champion-v3
    """

    def __init__(self, base):
        self.base = base

    def rotations(self, region=None):
        """Get list of Champion Rotations.
        """
        base_url = self.base.base_url[region]
        url = '{}/lol/platform/v3/champion-rotations'.format(base_url)
        r = requests.get(url, headers=self.base.headers)
        return r
