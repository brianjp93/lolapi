import requests


class LolStaticData:
    '''
    LOL-STATIC-DATA-V3
    https://developer.riotgames.com/api-methods/#lol-static-data-v3
    '''

    def __init__(self, base):
        self.base = base

    def champions(self, champion_id=None, region=None):
        '''
        get all champions if champion_id is not provided
        '''
        base_url = self.base.base_url[region]
        if champion_id is None:
            url = '{}/lol/static-data/v3/champions'.format(base_url)
        else:
            url = '{}/lol/static-data/v3/champions/{}'.format(base_url, champion_id)
        r = requests.get(url, headers=self.base.headers)
        return r

    def items(self, item_id=None, region=None):
        '''
        get all items if item_id is not provided
        '''
        base_url = self.base.base_url[region]
        if item_id is None:
            url = '{}/lol/static-data/v3/items'.format(base_url)
        else:
            url = '{}/lol/static-data/v3/items/{}'.format(base_url, item_id)

    def language_strings(self, region=None):
        '''
        Retrieve language strings data
        '''
        base_url = self.base.base_url[region]
        url = '{}/lol/static-data/v3/language-strings'.format(base_url)
        r = requests.get(url, headers=self.base.headers)
        return r

    def languages(self, region=None):
        '''
        Retrieve supported languages data
        '''
        base_url = self.base.base_url[region]
        url = '{}/lol/static-data/v3/languages'.format(base_url)
        r = requests.get(url, headers=self.base.headers)
        return r

    def maps(self, region=None):
        '''
        Retrieve map data
        '''
        base_url = self.base.base_url[region]
        url = '{}/lol/static-data/v3/maps'.format(base_url)
        r = requests.get(url, headers=self.base.headers)
        return r

    def masteries(self, masteries_id=None, region=None):
        '''
        masteries list or single id
        '''
        base_url = self.base.base_url[region]
        if masteries_id is None:
            url = '{}/lol/static-data/v3/masteries'.format(base_url)
        else:
            url = '{}/lol/static-data/v3/masteries/{}'.format(base_url, masteries_id)
        r = requests.get(url, headers=self.base.headers)
        return r

    def profile_icons(self, region=None):
        '''
        Retrieve profile icons
        '''
        base_url = self.base.base_url[region]
        url = '{}/lol/static-data/v3/profile-icons'.format(base_url)
        r = requests.get(url, headers=self.base.headers)
        return r

    def realms(self, region=None):
        '''
        get realm data
        '''
        base_url = self.base.base_url[region]
        url = '{}/lol/static-data/v3/realms'.format(base_url)
        r = requests.get(url, headers=self.base.headers)
        return r

    def runes(self, runes_id=None, region=None):
        '''
        get list of rune pages or single page by id
        '''
        base_url = self.base.base_url[region]
        if runes_id is None:
            url = '{}/lol/static-data/v3/runes'.format(base_url)
        else:
            url = '{}/lol/static-data/v3/runes/{}'.format(base_url, runes_id)
        r = requests.get(url, headers=self.base.headers)
        return r

    def summoner_spells(self, spell_id=None, region=None):
        '''
        '''
        base_url = self.base.base_url[region]
        if spell_id is None:
            url = '{}/lol/static-data/v3/summoner-spells'.format(base_url)
        else:
            url = '{}/lol/static-data/v3/summoner-spells/{}'.format(base_url, spell_id)
        r = requests.get(url, headers=self.base.headers)
        return r

    def versions(self, region=None):
        '''
        '''
        base_url = self.base.base_url[region]
        url = '{}/lol/static-data/v3/versions'.format(base_url)
        r = requests.get(url, headers=self.base.headers)
        return r