# Assisted by WCA for GP
# Latest GenAI contribution: granite-20B-code-instruct-v2 model
import json
import AIPFixturesRequest

from AIPFixturesRequest import fixtureListForRound

def saveFixtures (fixtures, filename):
    print ("oops not written yet")

# @TODO Somehow surface the filename (as return value rather than fixture list?) and print fixtures
#       based on that filename

def printFixtures (fixtures):

    # Open the file and read the data
    # with open('/Users/joc/Education/WCA/Fixtures.json', 'r') as f:
    #     data = json.load(f)

        # Loop through each fixture in the data
        for fixture in fixtures['response']:
            # Print the home and away teams
            print(f"Kickoff: {fixture['fixture']['date']}")
            print(f"Home Team: {fixture['teams']['home']['name']}")
            print(f"Away Team: {fixture['teams']['away']['name']}")
            print()


# fixtures = AIPFixturesRequest.fixtureListForRound (2023, 39, 29)
# printFixtures (fixtures)
# saveFixtures (fixtures, '/Users/joc/Education/WCA/Fixtures.json')
print("In module products __package__, __name__ ==", __package__, __name__)

fixtures = AIPFixturesRequest.fixtureListForDateRange (2023, 39, "2024-03-30", "2024-04-02")
printFixtures (fixtures)
fixtures = AIPFixturesRequest.fixtureListForDateRange (2023, 39, "2024-03-30", "2024-04-02")
printFixtures (fixtures)
fixtures = AIPFixturesRequest.fixtureListForDateRange (2023, 39, "2024-03-30", "2024-04-09")
printFixtures (fixtures)
fixtures = AIPFixturesRequest.fixtureListForRound (2023, 39, 1)
printFixtures (fixtures)
fixtures = AIPFixturesRequest.fixtureListForRound (2023, 39, 1)
printFixtures (fixtures)
fixtures = AIPFixturesRequest.fixtureListForRound (2023, 39, 2)
printFixtures (fixtures)
# saveFixtures (fixtures, '/Users/joc/Education/WCA/Fixtures.json')
# fixtures = AIPFixturesRequest.fixtureListForDateRange (2023, 39, "2024-04-23", "2024-04-25")
# printFixtures (fixtures)
# saveFixtures (fixtures, '/Users/joc/Education/WCA/Fixtures.json')
# fixtures = AIPFixturesRequest.fixtureListForDateRange (2023, 39, "2024-04-23", "2024-05-25")
# printFixtures (fixtures)
# saveFixtures (fixtures, '/Users/joc/Education/WCA/Fixtures.json')
