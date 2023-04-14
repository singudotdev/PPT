import dns.query
import dns.zone

target_ip = input("Insert target: ")
attackers_ip_domain = input("Insert your IP or Domain: ")

zone = dns.zone.from_xfr(dns.query.xfr(target_ip, attackers_ip_domain))
