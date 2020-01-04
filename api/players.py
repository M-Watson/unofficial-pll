import requests
import pandas as pd

def get_all_players():
    url = 'https://dn0a11v09sa0t.cloudfront.net/_Internal/Players.json'
    req = requests.get(url)
    return(req.json())

def get_player_stats(player_id, team = 'UNK'):
    if team == 'UNK':
        team_short_hand = ['ARC','ATL','CHA','CHR','RED','WHP']
        team_found = False
        num_of_teams = len(team_short_hand)
        team_index = 0
        while team_found == False:
            try:
                url = "https://dn0a11v09sa0t.cloudfront.net/Teams/{}/{}.json".format(team_short_hand[team_index],str(player_id))
                req = requests.get(url)
                req = req.json()
                team_found = True
            except:
                if team_index <= num_of_teams:
                    team_index += 1
                else:
                    req = 'ERR_GET_PLAYER_STATS_NOT_EXPLICIT_TEAM'
                    team_found = True
                    break
    else:
        team_short_hand = team
        try:
            url = "https://dn0a11v09sa0t.cloudfront.net/Teams/{}/{}.json".format(team_short_hand,str(player_id))
            req = requests.get(url)
            req = req.json()
            team_found = True
        except:
            print('Player and team combo not found, try running request without explicity team choice')
            req = 'ERR_GET_PLAYER_STATS_EXPLICITY_TEAM'
    return(req)
