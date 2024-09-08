import sendEmail
import datetime
import requests
import time

print(datetime.datetime.now())
waitTime = datetime.datetime.now() + datetime.timedelta(minutes= 10)
print(waitTime)
while(True):
    userID =  '996587741225889792'
    currUserID = requests.get('https://api.sleeper.app/v1/user/MBurnes')
    currNFLState = requests.get('https://api.sleeper.app/v1/state/nfl')
    currRosters = requests.get('https://api.sleeper.app/v1/league/1125590030598131712/rosters')
    currJSON = requests.get("https://api.sleeper.app/v1/league/1125590030598131712/matchups/" + str(currNFLState.json()['week']))
    week = currNFLState.json()['week']
    currRosters = requests.get('https://api.sleeper.app/v1/league/1125590030598131712/rosters')
    for roster in currRosters.json():
        #   print(roster)
          if roster['owner_id'] == userID:
                myRosterId = roster['roster_id']
    
    for matchup in currJSON.json():
            if matchup['roster_id'] == myRosterId:
                  matchID = matchup['matchup_id']
                  currPoints = matchup['points']

    
    while(week == requests.get('https://api.sleeper.app/v1/state/nfl').json()['week']):
          #wait for a minute
          matchupState = currJSON = requests.get("https://api.sleeper.app/v1/league/1125590030598131712/matchups/" + str(currNFLState.json()['week'])).json()
          for matchup in matchupState:
                if matchup['roster_id'] == myRosterId:
                      if (currPoints < matchup['points']):
                            currPoints = matchup['points']
                            sendEmail()
                            print(currPoints)
                            time.sleep(60)


#make this into a sportsbetting predictor?