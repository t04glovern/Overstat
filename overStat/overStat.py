import requests

class OverStatAPI:
    def __init__(self, key):
        self.key = key  # key to future proof API

    def get_stats(self, battle_tag):
        return self._make_request(
            'v2',
            battle_tag,
            'stats'
        )

    def get_hero(self, battle_tag, hero_id):
        return self._make_request(
            'v1',
            battle_tag,
            'heroes/' + hero_id,
        )

    def validate_response(self, response):
        if response.status_code != 200:
            raise Exception

    def sanitize_battletag(self, battle_tag):
        if '#' in battle_tag:
            battle_tag = battle_tag.replace('#','-')
        return battle_tag

    def _make_request(self, api_version,battle_tag, url):
        battle_tag = self.sanitize_battletag(battle_tag)
        r = requests.get(
            'https://owapi.net/api/{api_version}/u/{battle_tag}/{url}'.format(
                api_version = api_version,
                battle_tag = battle_tag,
                url = url
            )
        )
        self.validate_response(r)
        return r.json()