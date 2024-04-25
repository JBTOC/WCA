import pip._vendor.requests as requests
import os
import json

from PrivateKeys import my_API_Key


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
    if fixtureRoundStored (season, league, round):
        print ("Fixtures have already been fetched and stored")
        jsonFixtures = getFixturesRound (season, league, round)
    else:
        print ("Fixtures have NOT yet been fetched and stored")
        roundNumAsString = f'Regular Season - {round}'
        params = {'season': season, 'league': league, 'round': roundNumAsString}
        response = requests.get(url=url,
                params=params,
                headers=headers)
        jsonFixtures = response.json()
        storeFixturesRound (jsonFixtures, season, league, round)
    return jsonFixtures

def fixtureListForDateRange (season, league, fromDate, toDate):
    if fixtureDatesStored (season, league, fromDate, toDate):
        print ("Fixtures have already been fetched and stored")
        jsonFixtures = getFixturesDates (season, league, fromDate, toDate)
    else:
        print ("Fixtures have NOT yet been fetched and stored")
        params = {'season': season, 'league': league, 'from': fromDate, 'to': toDate}
        response = requests.get(url=url,
                params=params,
                headers=headers)
        jsonFixtures = response.json()
        storeFixturesDates (jsonFixtures, season, league, fromDate, toDate)
    return jsonFixtures


# Write a Python method called fixtureRoundStored that does the following…

# takes four parameters: year, league, fromDate, toDate.
# checks if file exists in the project’s storage folder. it is based on the filename of the four params concatenated
# if it exists it returns True othewise False

def fixtureDatesStored (season, league, fromDate, toDate):
    filename = f'{season}-{league}-{fromDate}-{toDate}.json'
    filepath = os.path.join('storage', filename)
    return os.path.exists(filepath)

# Write a Python method called fixtureRoundStored that  does the following…
# takes three parameters: year, league and round.
# checks if file exists in the project’s storage folder. it is based on the filename of the three params concatenated
# if it exists it returns True othewise False
def fixtureRoundStored (season, league, round):
    filename = f'{season}-{league}-{round}.json'
    filepath = os.path.join('storage', filename)
    return os.path.exists(filepath)

# Write a block of code in Python that takes a filepath then opens that file,
# reads the file contents into a json object and 
# returns that json object
def getFixturesRound (season, league, round):
    filename = f'{season}-{league}-{round}.json'
    filepath = os.path.join('storage', filename)
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data

def getFixturesDates (season, league, fromDate, toDate):
    filename = f'{season}-{league}-{fromDate}-{toDate}.json'
    filepath = os.path.join('storage', filename)
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data

def storeFixturesRound (jsonfixtures, season, league, round):
    
    filename = f'{season}-{league}-{round}.json'
    filepath = os.path.join('storage', filename)
    with open(filepath, 'w') as file:
        json.dump(jsonfixtures, file)

def storeFixturesDates (jsonfixtures, season, league, fromDate, toDate):
    
    filename = f'{season}-{league}-{fromDate}-{toDate}.json'
    filepath = os.path.join('storage', filename)
    with open(filepath, 'w') as file:
        json.dump(jsonfixtures, file)