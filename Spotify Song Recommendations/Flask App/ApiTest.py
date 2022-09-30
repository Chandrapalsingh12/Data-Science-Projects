import requests
from re import sub




def get_song_details(ids):
    headers = {
"X-RapidAPI-Key": "bcf46a0d4dmsh548b3c3c39ac8aap150bddjsn2d66c886abc8",
"X-RapidAPI-Host": "spotify23.p.rapidapi.com"
}
    url = "https://spotify23.p.rapidapi.com/tracks/"
    querystring = {"ids":ids}
    response = requests.request("GET", url, headers=headers, params=querystring)
    val = []
    val.append(response.text)
    
    data = []
    for i in val:
        dk = sub("[^A-Za-z0-9-?=:_,./ ]","",i)
        for j in dk.split(","):
            data.append(j)
    name=[]
    url = []
    prev_url = []
    listen_song = []
    track_id = []
    for i in data:
        if "name" in str(i):
            name.append(i)

        if "url:" in str(i):
            url.append(i.replace("url:",""))

        if "preview_url:" in str(i):
            prev_url.append(i.replace("preview_url:",""))
        
        if "uri:spotify:track" in str(i):
            listen_song.append(i.replace("uri:",""))

        if "id:" in str(i):
            track_id.append(i.replace("id:",""))

    return url[0],prev_url[0],listen_song[0],name[-1],track_id[-1]