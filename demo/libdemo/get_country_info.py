import requests

code = input("Enter country code :")
resp = requests.get(f"https://restcountries.eu/rest/v2/alpha/{code}")

if resp.status_code != 200:
    print("Could not get information about country!")
    exit(1)

country = resp.json()    # JSON to dict

print("Name        : ", country['name'])
print("Capital     : ", country['capital'])
print("Population  : ", country['population'])
print("Size (sqkm) : ", country['area'])

