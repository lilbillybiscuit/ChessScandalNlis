import requests
import json
import datetime

from objects import RatingObj
#id_list = open("player_ids.txt", "r")


def download_json(id):
    url = "https://ratings.fide.com/a_chart_data.phtml?event="+str(id)+"&period=0"
    print(url)
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
            ret.append(RatingObj(obj).toJSON())
        return ret

# res = parse_player(1503014)
# for obj in res:
#     print(obj)