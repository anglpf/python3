# create a mapping of state to abbreviation
states = {
    'Essex': 'ESX',
    'Buckinghamshire': 'BCK',
    'Cumbria': 'CBR',
    'Oxfordshire': 'OXF',
    'Dorset': 'DOR'
}

# create a basic set of states and some cities in them
cities = {
    'ESX': 'Dunmow',
    'BCK': 'Beaconsfield',
    'CBR': 'Ambleside'
}

# add some more cities
cities['OXF'] = 'Benson'
cities['DOR'] = 'Portland'

# print out some cities
print('-' * 10)
print("ESX County has: ", cities['ESX'])
print("DOR County has: ", cities['DOR'])

# print some states
print('-' * 10)
print("Buckinghamshire's abbreviation is: ", states['Buckinghamshire'])
print("Cumbria's abbreviation is: ", states['Cumbria'])

# do it by using the state then cities dict
print('-' * 10)
print("Essex has: ", cities[states['Essex']])
print("Dorset has: ", cities[states['Dorset']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in every state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev} and has city {cities[abbrev]}")

print('-' * 10)
# safely get an abbreviation by state that might not be there.
county_not_included = 'London'
state = states.get(county_not_included)

if not state:
    print(f"Sorry, no {county_not_included}.")

# get a city with a default value
city = cities.get('LON', 'Does Not Exist')
print(f"The city for the state 'LON' is: {city}")

"""
Bear in mind: dictionaries have no order.
"""
