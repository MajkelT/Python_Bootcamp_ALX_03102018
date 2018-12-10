# www.metaweather.com/api
# /api/location/search/?query=(query)
# /api/location/(woeid)/

import json
# import urllib.request
from urllib.request import urlopen

miasto = input("Podaj nazwe miasta: ")
with urlopen(f"https://www.metaweather.com/api/location/search/?query={miasto}") as file:
    warszawa = json.loads(file.read().decode("utf-8"))   #json zaladuj z napisu...  --> lista bedaca slownikiem
    ID = (warszawa[0]["woeid"])
with urlopen(f"https://www.metaweather.com/api/location/{ID}/") as file:
    data = json.loads(file.read().decode("utf-8"))
    print(data)
    prognozy = data['consolidated_weather']
    for prognoza in prognozy:
        print(f"Dzień: {prognoza['applicable_date']}")
        print(f"Temperatura: {prognoza['the_temp']:.1f}")  #.1f zaokragla do 1 miejsca po przecinu
        print(f"Wilgotność: {prognoza['humidity']}%")
        print()  #wstawia pusty wiersz



#with urlopen("https://www.metaweather.com/api/location/search/?query=Warsaw") as file:
#print(warszawa)   #[{'title': 'Warsaw', 'location_type': 'City', 'woeid': 523920, 'latt_long': '52.235352,21.009390'}]
#print(warszawa[0]["title"])  #Warsaw
#print(warszawa[0]["woeid"])  #523920

