import pip._vendor.requests as requests
from .PrivateKeys import my_API_Key


# my_API_Key = PrivateKeys.my_API_Key


headers = {
    'x-rapidapi-host': "https://v3.football.api-sports.io/",
    'x-rapidapi-key': my_API_Key
    }

#params = {'season': 2023, 'league': 39, 'round': "Regular Season - 30"}
url = "https://v3.football.api-sports.io/fixtures"

#return jsonFixtures
##
# The function fixtureListForRound takes in three parameters: 
# season, league, and round. 
# It uses these parameters to construct a request URL using the requests library.
# The request is made to the NHL (Wrong - its football ie Premier League) API, 
# which returns a JSON object containing information about the fixtures for the specified round.
# Finally, the function returns the JSON object.
##

def fixtureListForRound (season, league, round):
    roundNumAsString = f'Regular Season - {round}'
    params = {'season': season, 'league': league, 'round': roundNumAsString}
    response = requests.get(url=url,
             params=params,
             headers=headers)
    jsonFixtures = response.json()
    return jsonFixtures

def fixtureListForDateRange (season, league, fromDate, toDate):
    params = {'season': season, 'league': league, 'from': fromDate, 'to': toDate}
    response = requests.get(url=url,
             params=params,
             headers=headers)
    jsonFixtures = response.json()
    return jsonFixtures
