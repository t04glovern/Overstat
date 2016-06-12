import urllib3
import simplejson as json
import csv
import sys
import re


def requestStats():
    print('Enter Battle.net ID [UserName#1234]')
    _name = input()

    # Convert # String to correct API format
    _username = re.sub('#', '-', _name, 0)

    print('Enter your Platform [pc,xbl,psn]')
    _platform = input()

    print('Enter your Region [eu,us]')
    _region = input()

    _http = urllib3.PoolManager()
    _request = _http.request('GET', 'https://api.lootbox.eu/' + _platform + '/' + _region + '/' + _username + '/heroes')
    _json_data = json.loads(_request.data)

    for item in _json_data:
        print(item['name'], item['playtime'], str(item['percentage']))

if __name__ == "__main__":
    # Disable cert warnings
    urllib3.disable_warnings()
    requestStats()