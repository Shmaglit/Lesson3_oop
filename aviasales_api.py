#1. Написать функцию получения IATA-кода города из его названия, используя API Aviasales.

import requests
import json

city = input('Введите название города на русском языке:')
link = f'http://autocomplete.travelpayouts.com/places2?term={city}&locale=ru&types[]=city'
data = json.loads(requests.get(link).text, encoding='utf-8 ')
iata = data[0]['code']
print(f'IATA код: {iata}')
