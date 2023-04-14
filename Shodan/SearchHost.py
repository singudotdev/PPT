import shodan


def ShodanSearchHost():
    try:
        ShodanApi = shodan.Shodan(input("Insert your API key: "))

        results = ShodanApi.host(input("Target: "))

        for result in results:
            print("%s: %s" % (result, results[result]))
    except shodan.APIError as e:
        print("Error: %s" % e)


if __name__ == "__main__":
    ShodanSearchHost()
