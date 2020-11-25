import json
import urllib3

# print(getTotalGoals("Chelsea", 2014))
name = "UEFA Champions League"
year = '2011'
def getTotalGoals(name, year):
    goal = 0
    url = "https://jsonmock.hackerrank.com/api/football_competitions?name={0}&year={1}"
    urls = ["https://jsonmock.hackerrank.com/api/football_matches?competition={0}&year={1}&team1={2}&page={3}", 
    "https://jsonmock.hackerrank.com/api/football_matches?competition={0}&year={1}&team2={2}&page={3}"]
    poolMan = urllib3.PoolManager()
    winner = ''
    req = poolMan.request("GET", url.format(name, year))
    dec = json.loads(req.data.decode('utf-8'))['data'][0]
    winner = dec['winner']
    
    for curl in urls:
        print(curl.format(name, year, winner, 1))
        i = 1
        hasData = True
        while hasData != False:
            sec_req = poolMan.request("GET", curl.format(name, year, winner, i))
            dec = json.loads(sec_req.data.decode('utf-8'))['data']
            if dec == []:
                hasData = False
                i = 1
            else:
                for vals in dec:
                    if vals['team1'] == winner:
                        goal += int(vals['team1goals'])
                    if vals['team2'] == winner:
                        goal += int(vals['team2goals'])
                
                i += 1


    return goal

getTotalGoals(name, year)