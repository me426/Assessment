import requests
import sys

city = sys.argv[1]

url = 'http://api.openweathermap.org/data/2.5/weather?q={0}&appid=8bf383a4b3b406f2cdebe6e74a296873&units=metric'.format(city)

res = requests.get(url)

data = res.json()

temp = data['main']['temp']
country = data['sys']['country']

print('Temperature for {},{} is {} \u2103 '.format(city, country, temp))
