import matplotlib.pyplot as plt
import pprint
import ipinfo
import numpy as np

file = open("ip.txt", "r")
cities = {}
countries = {}

while True:
    ip_address = file.readline()
    access_token = 'f2d819853a8505'
    handler = ipinfo.getHandler(access_token)
    if not ip_address:
        break
    ip_address = ip_address.strip()
    details = handler.getDetails(ip_address)
    if "city" in details.all.keys():
        if details.city is not None:
            if details.city not in cities.keys():
                cities[details.city] = 1
            else:
                cities[details.city] += 1
    if "country_name" in details.all.keys():
        if details.country_name is not None:
            if details.country_name not in countries.keys():
                countries[details.country_name] = 1
            else:
                countries[details.country_name] += 1

file.close()
cities_procents = []
counrtries_procents = []
cities_numbers = []
counrtries_numbers = []
count_city = 0
count_country = 0
summ_city = 0
summ_country = 0

for i in cities.values():
    summ_city += i
    count_city += 1
    cities_numbers.append(count_city)

for i in countries.values():
    summ_country += i
    count_country += 1
    counrtries_numbers.append(count_country)

for i in cities.values():
    cities_procents.append((i * 100) / summ_city)

for i in countries.values():
    counrtries_procents.append((i * 100) / summ_country)

city = []
country = []
count_city = 0
count_country = 0

for key in cities.keys():
    count_city += 1
    city.append(str(count_city) + " " + str(key))

for key in countries.keys():
    count_country += 1
    country.append(str(count_country) + " " + str(key))

plt.pie(cities_procents, labels=cities_numbers, labeldistance=1.09, startangle=90, radius=1, textprops={'fontsize': 7})
plt.legend(labels=city, loc='lower left', fontsize=7)
plt.show()

plt.pie(counrtries_procents, labels=counrtries_numbers, labeldistance=1.09, startangle=90, radius=1,
        textprops={'fontsize': 7})
plt.legend(labels=country, loc='lower left', fontsize=7)
plt.show()
