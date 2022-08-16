from statistics import mode
from flask import Flask,render_template,request

import pickle

model = pickle.load(open("model.pkl",'rb'))
tfid = pickle.load(open("vector.pkl",'rb'))


 

def prep_txt(w):
    import re
    q = re.sub("[^a-zA-Z0-9 ]","",w)
    q = q.lower()
    q = q.split(" ")
    from nltk.corpus import stopwords
    sw = stopwords.words("english")
    from nltk.stem import PorterStemmer
    ps = PorterStemmer()
    # wnl = WordNetLemmatizer()
    r = ""
    for i in q:
        if(i not in sw):
            t = ps.stem(i)
            r = r + " " + t
    return r


app = Flask(__name__)


@app.route('/', methods =["GET", "POST"])
def home():
    if request.method == "POST":
        email = request.form.get("email")   
        val = prep_txt(email)
        inps = tfid.transform([val]).toarray()
        pred = model.predict(inps)[0]
        
        data = pred

        return render_template("index.html",data=data)

        
       
    return render_template("index.html")

   
app.run(debug = True)