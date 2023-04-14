import shodan


def ShodanInfo():
    try:
        ShodanApi = shodan.Shodan(input("Insert your API key: "))

        results = ShodanApi.info()

        for info in results:
            print(info, ": ", results[info])
    except shodan.APIError as e:
        print("Error: %s" % e)


if __name__ == "__main__":
    ShodanInfo()
