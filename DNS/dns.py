import dns.resolver

target = input("Insert target: ")

ansA = dns.resolver.resolve(target, "A")
ansMX = dns.resolver.resolve(target, "MX")
ansNS = dns.resolver.resolve(target, "NS")
ansAAAA = dns.resolver.resolve(target, "AAAA")

print(ansA.response.to_text())
print()
print(ansMX.response.to_text())
print()
print(ansNS.response.to_text())
print()
print(ansAAAA.response.to_text())
