cities = ("Kolkata", "Delhi", "Mumbai", "Chennai", "Kolkata")

print("All cities:", cities)

print("First two cities:", cities[:2])

for city in cities:
    if cities.count(city) == 2:
        print("City present twice:", city)
        break