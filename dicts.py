#dict
weather = {'city':'Москва', 'temp':25, 'wind':'восточный'}
print(weather['city'])
weather['city']

#print(weather['contry'])
print(weather.get('county'))

weather['date']='27.05.2017'
#weather['date']
print(weather['date'])

weather_list = [
    {'city':'Москва', 'temp':-2, 'wind':'восточный', 'date':'01.01.2018'},
    {'city':'Москва', 'temp':20, 'wind':'восточный', 'date':'01.05.2018'}
]
print(weather_list)

weather_list.append(weather)
print(weather_list)
##########



