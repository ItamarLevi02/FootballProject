import requests
from bs4 import BeautifulSoup

url = 'https://www.footballdb.com/games/index.html?lg=NFL&yr=2023'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'}

# Send the request with the custom headers
r = requests.get(url, headers=headers)

# Print the status code to check the response
soup = BeautifulSoup(r.text, 'html.parser')

league_table = soup.find('table',class_ = 'statistics')

Teams = []
Scores=[]

for team in league_table.find_all('tbody'):
    rows = team.find_all('tr')
    for row in rows:
        gameData = row.find_all('td')
        for teams in gameData:
            teamInfo = teams.find('span',class_='visible-xs-inline')
            if teamInfo != None:    
                Teams.append(teamInfo.text)
        HomeScore = row.find_all('td',class_="center")[0].text
        AwayScore = row.find_all('td',class_="center")[1].text

        Scores.append([HomeScore,AwayScore])
    
        
print(Teams)
print(Scores)

        
            

            
                

            
        
