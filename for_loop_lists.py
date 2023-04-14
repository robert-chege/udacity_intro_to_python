# Creating a new list 
cities = ['new york city', 'los angeles', 'mountain view', 'chicago']
capitalized_cities = []

for city in cities:
    capitalized_cities.append(city.title())

print(capitalized_cities)

# Modifying a list
for index in range(len(cities)):
    cities[index] = cities[index].title()

print(cities)