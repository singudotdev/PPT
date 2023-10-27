import whois

target = input("Insert target: ")

whoisResponse = whois.whois(target)

print(whoisResponse)
