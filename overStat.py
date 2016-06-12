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


def compareStats(_user1, _user2, _platform, _region):
    _username1 = re.sub('#', '-', _user1, 0)
    _username2 = re.sub('#', '-', _user2, 0)

    _http = urllib3.PoolManager()
    _request1 = _http.request('GET', 'https://api.lootbox.eu/' + _platform + '/' + _region + '/' + _username1 + '/profile')
    _request2 = _http.request('GET', 'https://api.lootbox.eu/' + _platform + '/' + _region + '/' + _username2 + '/profile')
    _json_data1 = json.loads(_request1.data)
    _json_data2 = json.loads(_request2.data)

    print('Username: ',_json_data1['data']['username'],'\t',
          'Playtime: ',_json_data1['data']['playtime'],'\t',
          'Wins: ',_json_data1['data']['games']['wins'],'\t',
          'Lost: ',_json_data1['data']['games']['lost'],'\t',
          'Win Percentage: ',_json_data1['data']['games']['win_percentage']
          )
    print('Username: ', _json_data2['data']['username'],'\t',
          'Playtime: ', _json_data2['data']['playtime'],'\t',
          'Wins: ', _json_data2['data']['games']['wins'],'\t',
          'Lost: ', _json_data2['data']['games']['lost'],'\t',
          'Win Percentage: ', _json_data2['data']['games']['win_percentage']
          )


if __name__ == "__main__":
    # Disable cert warnings
    urllib3.disable_warnings()

    compareStats('UserName1#1234', 'UserName2#1234', 'pc', 'us')