from bs4 import BeautifulSoup
import requests
from scrape_rating_graphs import parse_player
import json
from objects import PlayerObj, serialize

url = "https://ratings.fide.com/incl_search_l.php?search=&search_rating=all&search_country=all&search_title=all&search_other_title=all&search_year=undefined&search_low=2700&search_high=3500&search_inactive=off&search_exrated=off&search_radio=undefined&search_bday_start=all&search_bday_end=all&search_radio=undefined&search_asc=undefined&search_gender=undefined&simple=0"

req = requests.get(url,headers={
    "X-Requested-With": "XMLHttpRequest"
})
soup = BeautifulSoup(req.text, "html.parser")

table = soup.find("tbody")
rows = table.find_all("tr")
results = []
fileoutput = open("player_ids.txt", "w")
count=0
for row in rows:
    if count>=5:
        break
    count+=1
    link = row.find("a")
    player_id = link['href'].split("/")[-1]
    res = parse_player(player_id)
    results.append({
        "id": player_id,
        "data": res
    })
print(results)
fileoutput.write(json.dumps(results))
fileoutput.close()