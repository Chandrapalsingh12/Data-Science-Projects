import re
from flask import Flask,render_template,request
import pickle
from ApiTest import get_song_details


app = Flask(__name__)

df = pickle.load(open("dataset.pkl",'rb'))
model = pickle.load(open("model.pkl",'rb'))


new_df = df.track_name.tolist()

@app.route("/",methods =["GET", "POST"])
def home():
    if request.method=="POST":
        song = request.form.get("song")
        song_ind = df[df.track_name==song].index[0]
        song_sim = model[song_ind]
        song_list = sorted(list(enumerate(song_sim)),reverse=True,key=lambda x:x[1])[0:6]

        song_data =[]
        track_id = []
        track_album_id = []
        playlist_id = []
        for i in song_list:
            song_data.append(df.iloc[i[0]].track_name)
            track_id.append(df.iloc[i[0]].track_id)
            track_album_id.append(df.iloc[i[0]].track_album_id)
            playlist_id.append(df.iloc[i[0]].playlist_id)

        song_details = track_id[0]
        url1,prev_url,full_url,name,t_url = get_song_details(song_details)

        recom_song = []
        for i in track_id[1:]:
            recom_song.append(get_song_details(i))       
        
        return render_template("index.html",song=new_df,data=song_data[1:],c_son=song,t_id=track_id[1:],ta_id=track_album_id[1:],p_id=playlist_id[1:],
        img_url=url1,prev_song=prev_url,full_url=full_url,song_name=name,
        recom_song=recom_song
        )


    return render_template("index.html",song=new_df)

@app.route("/<t_id>")
def recon(t_id):
    song_ind = df[df.track_id==t_id].index[0]
    song_sim = model[song_ind]
    song_list = sorted(list(enumerate(song_sim)),reverse=True,key=lambda x:x[1])[0:6]

    song_data =[]
    track_id = []
    track_album_id = []
    playlist_id = []
    for i in song_list:
        song_data.append(df.iloc[i[0]].track_name)
        track_id.append(df.iloc[i[0]].track_id)
        track_album_id.append(df.iloc[i[0]].track_album_id)
        playlist_id.append(df.iloc[i[0]].playlist_id)

    song_details = track_id[0]
    url1,prev_url,full_url,name,t_url = get_song_details(song_details)

    recom_song = []
    for i in track_id[1:]:
        recom_song.append(get_song_details(i))       
    
    return render_template("index.html",song=new_df,data=song_data[1:],t_id=track_id[1:],ta_id=track_album_id[1:],p_id=playlist_id[1:],
    img_url=url1,prev_song=prev_url,full_url=full_url,song_name=name,
    recom_song=recom_song
    )


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80,debug=True)
   
