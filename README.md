![Coverage Badge](./coverage.svg)

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
>>> api.spectator
>>> api.summoner
>>> api.thirdpartycode
>>> api.tftleague
>>> api.tftmatch
>>> api.tftsummoner
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

# Testing

Testing requires `pytest-cov`, `pytest`, and `coverage`

Tests can be run using just pytest
```
>>> pytest
```

Or with coverage
```
>>> pytest --cov=lol ./
```

Add coverage badge with
```
>>> coverage-badge
```
