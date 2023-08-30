# Goals for this:
# This should take information from a text file that contains the following: 
# The current D-SHT #, the default schedule information, and the JSON template
# It shows these in the standard announcement form, and requests any adjustment
# Then replace any JSON placeholders for each game
#   (API KEY, D-SHT #, The date + start time, and the game played)
# Finally call the challonge API to create the brackets


#! Python 3
# makeChallonge.py is to make challonge brackets for the weekly events

import requests, json

# The current D-SHT number, load in somehow----------
dshtNumber = # Load this in from the hidden data json perhaps?
# The data getting sent with the post request, I think it's the API key?----------
data = # load the API key here
# The URL for the Challonge API, maybe worth also loading in
apiURL = 'https://api.challonge.com/v1/tournaments.json'

# The template json to start with, load in api_key somehow from somewhere private----------
challongeTemplate = {
    "tournament":{
        "name": "D-SHT (NUMBER) (EVENT TYPE)",
        "tournament_type": "double elimination", 
        "url": "DSHT(NUMBER)(EVENT TYPE)",
        "description": "Maybe I use this??",
        "start_at": "(EVENT TYPE START TIME)"    
    }
}

# Make something to create the name, url, and start time----------

# Function to make an individual challonge bracket given the event type and start time----------
makeBracket(eventType, startTime):
    challongeTemplate[name] = "D-SHT " + str(dshtNumber) + " " + eventType
    challongeTemplate[url] = "DSHT"+str(dshtNumber)+eventType
    challongeTemplate[start_at] = 
    challongeJson = json.dumps(challongeTemplate)
    # requests.post(apiURL, data, challongeJson)

