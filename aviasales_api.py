import requests
import json


#link2 = 'https://www.travelpayouts.com/widgets_suggest_params?q=Из%20Москвы%20в%20Лондон'
city = input('Введите название города на русском языке:')
link = f'http://autocomplete.travelpayouts.com/places2?term={city}&locale=ru&types[]=city'
data = json.loads(requests.get(link).text, encoding='utf-8 ')
iata = data[0]['code']
print(f'IATA код: {iata}')
