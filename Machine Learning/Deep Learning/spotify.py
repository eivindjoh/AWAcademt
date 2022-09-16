import requests
import json

url = "https://spotify23.p.rapidapi.com/user_profile/"

querystring = {"id":"eivindaj","playlistLimit":"10","artistLimit":"20"}

headers = {
	"X-RapidAPI-Key": "0710598afemsh8085b585dda9e06p18a40cjsn46ccdfa5414a",
	"X-RapidAPI-Host": "spotify23.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

user_data = response.json()

with open("user_spotify_tracks.json", "w") as fp:
    json.dump(user_data, fp)
