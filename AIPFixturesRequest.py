import pip._vendor.requests as requests

my_API_Key = "d0ced636d8212c0076ca83feb0b7dc11"

headers = {
    'x-rapidapi-host': "https://v3.football.api-sports.io/",
    'x-rapidapi-key': my_API_Key
    }

params = {'season': 2023, 'league': 39, 'round': "Regular Season - 29"}
url = "https://v3.football.api-sports.io/fixtures"

response = requests.get(url=url,
             params=params,
             headers=headers)
jsonFixtures = response.json()

#return jsonFixtures