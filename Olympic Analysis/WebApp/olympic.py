import re
from flask import Flask,render_template,request
import pickle
from Funmain import MainClass



app = Flask(__name__)

df = pickle.load(open("df.pkl",'rb'))

# Object of Medal
maincs = MainClass(df)






@app.route('/', methods =["GET", "POST"])
def home():
    medal_ta,year,country = maincs.medalmain()
    if request.method=="POST":
        val = request.form.get("Medel")         
        yr = request.form.get("year")
        cnt = request.form.get("country")

        cs = medal_ta
        print(cs)
        if yr!=None or cnt!=None:

            # cs = medal_tail(df,yr,cnt)
            cs = maincs.medal_tail(yr,cnt)
            return render_template("index.html",cs=cs,data=cs.to_html(),year=year,country=country)
        return render_template("index.html",cs=cs,data=cs.to_html(),year=year,country=country)
    return render_template("index.html",medal_ta=medal_ta,year=year,country=country,data=medal_ta.to_html())



@app.route('/overall', methods =["GET", "POST"])
def overall():
   
    Edition,city,sport,event,athlete,nation = maincs.overall()

    X,Y,X1,Y1,X2,Y2 = maincs.shoGraph()
    most_suc,sprt = maincs.most_sec("overall")

    if request.method=="POST":
        spr = request.form.get("sport")

        most_suc,_ = maincs.most_sec(sport=spr)

        
        

        return render_template("overall.html",ed=Edition,cty=city,sport=sport,evt=event,ath=athlete,nt=nation,most_suc=most_suc,X=X,Y=Y,X1=X1,Y1=Y1,X2=X2,Y2=Y2,data=most_suc.to_html(),sprt=sprt)

    return render_template("overall.html",ed=Edition,cty=city,sport=sport,evt=event,ath=athlete,nt=nation,X=X,Y=Y,X1=X1,Y1=Y1,X2=X2,Y2=Y2,most_suc=most_suc,data=most_suc.to_html(),sprt=sprt)


@app.route('/country', methods =["GET", "POST"])
def country():
    c_name = maincs.get_country_name()

    if request.method=="POST":
        cnme = request.form.get("country")
        c_year,c_medal = maincs.Medal_Taily_Country(cnme)
        most_ath= maincs.country_most(cnme)

        return render_template("country.html",c_year=c_year,c_medal=c_medal,cnme=cnme,c_name=c_name,most_ath=most_ath,data=most_ath.to_html())
    
    return render_template("country.html",c_name=c_name)

    
@app.route('/athlete', methods =["GET", "POST"])
def athlete():
    x1,x2,x3,x4 = maincs.Athlete()
    Y,X1,X2 = maincs.male_female()

   
    return render_template("athlete.html",x1=x1,x2=x2,x3=x3,x4=x4,Y=Y,X1=X1,X2=X2)


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80,debug=True)
   

