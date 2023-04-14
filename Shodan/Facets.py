import shodan

FACETS = [
    ("org", 15),
    ("domain", 15),
    ("port", 15),
    ("asn", 10),
    ("country", 15)
]

FACET_TITLES = {
    "org": "Top 15 Organizations",
    "domain": "Top 15 Domains",
    "port": "Top 15 Ports",
    "asn": "Top 10 Autonomous Systems",
    "country": "Top 15 Countries"
}

try:
    ShodanApi = shodan.Shodan(input("Insert your API key: "))
    result = ShodanApi.count(input("Search: "), facets=FACETS)
    print("Total results: %s\n" % result["total"])
    for facet in result["facets"]:
        print(FACET_TITLES[facet])
        for term in result["facets"][facet]:
            print(term["value"], term["count"])
        print("")

except Exception as e:
    print("Error: %s" % e)
