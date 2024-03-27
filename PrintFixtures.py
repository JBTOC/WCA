# Assisted by WCA for GP
# Latest GenAI contribution: granite-20B-code-instruct-v2 model
import json

# Open the file and read the data
with open('/Users/joc/Education/WCA/Fixtures.json', 'r') as f:
    data = json.load(f)

# Loop through each fixture in the data
for fixture in data['response']:
    # Print the home and away teams
    print(f"Home Team: {fixture['teams']['home']['name']}")
    print(f"Away Team: {fixture['teams']['away']['name']}")
    print()
