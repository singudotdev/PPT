import geoip2.database

db = 'GeoLite2City.mmdb'
lector = geoip2.database.Reader(db)

ip_address = input("Insert target: ")

response = lector.city(ip_address)

print(response.country.name)
print(response.subdivisions.most_specific.name)
print(response.city.name)
print(response.location.latitude)
print(response.location.longitude)
