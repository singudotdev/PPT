import geoip2.database

lector = geoip2.database.Reader('GeoLite2City.mmdb')

ip_address = input("Insert target: ")

response = lector.city(ip_address)

print(response.country.name)
print(response.subdivisions.most_specific.name)
print(response.city.name)
print(response.location.latitude)
print(response.location.longitude)
