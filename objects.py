import json
import datetime


class RatingObj:
    def intconvert(self, string):
        try:
            return int(string)
        except Exception:
            return None
    def __init__(self, obj):
        self.date = datetime.datetime.strptime(obj["date_2"], "%Y-%b").strftime("%Y-%m")
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
    def toJSON(self):
        return {
            "date": self.date,
            "id_number": self.id_number,
            "rating": self.rating,
            "period_games": self.period_games,
            "rapid_rating": self.rapid_rating,
            "rapid_games": self.rapid_games,
            "blitz_rating": self.blitz_rating,
            "blitz_games": self.blitz_games,
            "name": self.name,
            "country": self.country
        }
def serialize(obj):
    if isinstance(obj, RatingObj):
        return {
            "date": obj.date,
            "id_number": obj.id_number,
            "rating": obj.rating,
            "period_games": obj.period_games,
            "rapid_rating": obj.rapid_rating,
            "rapid_games": obj.rapid_games,
            "blitz_rating": obj.blitz_rating,
            "blitz_games": obj.blitz_games,
            "name": obj.name,
            "country": obj.country
        }
    return obj.__dict__

class PlayerObj:
    def intconvert(self, string):
        try:
            return int(string)
        except Exception:
            return None
    def __init__(self, arr):
        self.name = arr[0]
        self.title = arr[1]
        self.id = self.intconvert(arr[0])
        
        self.country = arr[2]
        self.rating = self.intconvert(arr[3])
        self.plusminus = arr[4]
        self.birthyear = self.intconvert(arr[5])
        self.avg12m = self.intconvert(arr[6][:4].strip())
    def __str__(self):
        return json.dumps({
            "id": self.id,
            "name": self.name,
            "country": self.country,
            "rating": self.rating,
            "plusminus": self.plusminus,
            "birthyear": self.birthyear,
            "avg12m": self.avg12m
        })
class PlayerObj2:
    def intconvert(self, string):
        try:
            return int(string)
        except Exception:
            return None
    def __init__(self, arr):
        self.id = self.intconvert(arr[0])
        self.name = arr[1]
        self.country = arr[2]
        self.rating = self.intconvert(arr[3])
        self.plusminus = arr[4]
        self.birthyear = self.intconvert(arr[5])
        self.avg12m = self.intconvert(arr[6][:4].strip())
    def __str__(self):
        return json.dumps({
            "id": self.id,
            "name": self.name,
            "country": self.country,
            "rating": self.rating,
            "plusminus": self.plusminus,
            "birthyear": self.birthyear,
            "avg12m": self.avg12m
        })
