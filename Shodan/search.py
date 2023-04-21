import shodan


def ShodanSearch():
    try:
        ShodanApi = shodan.Shodan(input("Insert your API key: "))

        results = ShodanApi.search(input("Search: "))

        for result in results['matches']:
            print('IP: %s' % result['ip_str'])
            print(result['data'])
            print('')
    except shodan.APIError as e:
        print("Error: %s" % e)


if __name__ == "__main__":
    ShodanSearch()
