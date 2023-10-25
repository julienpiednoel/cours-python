#!/usr/bin/env python
from datetime import datetime
from json import loads
from requests import get

timezone = input("Fuseau Horaire : ")
response = get('https://worldtimeapi.org/api/timezone/' + timezone)

if response.status_code != 200:
 raise ValueError('Erreur Fuseau horaire')

response_json = loads(response.text)

print(datetime.fromtimestamp(response_json['unixtime'] + response_json['raw_offset']))
