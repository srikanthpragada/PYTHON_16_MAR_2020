import requests

def get_area(v):
    return 0 if v is None else v

resp = requests.get("https://restcountries.eu/rest/v2/all")
countries = resp.json()

for c in sorted(countries, key=lambda v: v['population'], reverse=True)[:10]:
    print(f"{c['name']:50} {c['population']:12} {get_area(c['area']):10}")

