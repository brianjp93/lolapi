# League of Legends API Wrapper

**lolwrapper** is a Python wrapper for the Riot League of Legends API endpoints.
**lolwrapper** works with Python >= 3.6

# Installation

```bash
$ pip install lolwrapper
```

# Usage

```python
>>> from lol.riot import Riot
>>> 
>>> api = Riot('your-api-key')
```

## Available Resources

```python
>>> api.champion
>>> api.championmastery
>>> api.league
>>> api.lolstaticdata
>>> api.lolstatus
>>> api.masteries
>>> api.match
>>> api.runes
>>> api.spectator
>>> api.summoner
>>> api.thirdpartycode
```

### Get a summoner

* Get by name, encrypted account ID, encrypted summoner ID, or encrypted PUUID
```python
>>> r = api.summoner.get(name='tenmo player', region='na')
>>> r = api.summoner.get(encrypted_account_id='account-id', region='na')
>>> r = api.summoner.get(encrypted_summoner_id='summoner-id', region='na')
>>> r = api.summoner.get(encrypted_puuid='puuid', region='na')
>>> r.json()
```

