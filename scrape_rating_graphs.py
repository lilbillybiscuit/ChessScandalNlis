import requests
import json
import datetime

#id_list = open("player_ids.txt", "r")

class RatingObj:
    def intconvert(self, string):
        try:
            return int(string)
        except Exception:
            return None
    def __init__(self, obj):
        self.date = datetime.datetime.strptime(obj["date_2"], "%Y-%b").date()
        self.id_number = obj["id_number"]
        self.rating = self.intconvert(obj["rating"])
        self.period_games = obj["period_games"]
        self.rapid_rating = self.intconvert(obj["rapid_rtng"])
        self.rapid_games = obj["rapid_games"]
        self.blitz_rating = self.intconvert(obj["blitz_rtng"])
        self.blitz_games = obj["blitz_games"]
        self.name = obj["name"]
        self.country = obj["country"]
    
    def __str__(self):
        return f"{self.name} ({self.country}) - {self.date}: {self.rating}"
def download_json(id):
    url = "https://ratings.fide.com/a_chart_data.phtml?event="+str(id)+"&period=0"
    r = requests.post(url, headers={
      "X-Requested-With": "XMLHttpRequest"
    })
    if r.status_code == 200:
        json_data = json.loads(r.text)
        return json_data
    else:
        print("Error: " + r.status_code)
        return None

def parse_player(id):
    json_data = download_json(id)
    if json_data is None:
        return None
    else:
        ret = []
        for obj in json_data:
            ret.append(RatingObj(obj))
        return ret

print(parse_player(1503014)[0])