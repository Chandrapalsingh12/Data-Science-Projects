import re
from flask import Flask,render_template,request
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

A = pickle.load(open("ds.pkl",'rb'))
ohe = pickle.load(open("ohe.pkl",'rb'))
model = pickle.load(open("model.pkl",'rb'))

# Creating Object
brand = A.Company.unique()
Type = A.TypeName.unique()
Inches = A.Inches.unique()
Ram = A.Ram.unique()
OpSys = A.OpSys.unique()
Weight = A.Weight.unique()    
Resolution = A.Resolution.unique()
Touchscreen = A.Touchscreen.unique()
Ips_Panel = A.Ips_Panel.unique()
Processor_Name = A.Processor_Name.unique()
Processor_Generation = A.Processor_Generation.unique()
Ghz = A.Ghz.unique()
Storage_type = A.Storage_type.unique()
Storage_Size = A.Storage_Size.unique()
Gpu_Brand = A.Gpu_Brand.unique()
Gpu_Name = A.Gpu_Name.unique()


@app.route('/', methods =["GET", "POST"])
def home():
    if request.method == "POST":
        bs = request.form.get("brand")
        ts = request.form.get("Type")
        In = request.form.get("Inches")
        Rs = request.form.get("Resolution")
        Rm = request.form.get("Ram")
        Osy = request.form.get("OpSys")
        Wig = request.form.get("Weight")
        Ts = request.form.get("Touchscreen")
        Ips = request.form.get("Ips_Panel")
        Gz = request.form.get("Ghz")
        Pn = request.form.get("Processor_Name")
        Pg = request.form.get("Processor_Generation")
        St = request.form.get("Storage_type")
        Ss = request.form.get("Storage_Size")
        Gpu = request.form.get("Gpu_Brand")
        Gp_name = request.form.get("Gpu_Name")


        X = pd.DataFrame([bs,ts,In,Rs,Rm,Osy,Wig,Ts,Ips,Gz,Pn,Pg,St,Ss,Gpu,Gp_name]).T
        OHE = ohe.transform(X)

        Price = np.exp(model.predict(OHE))

        return render_template("index.html",Price=Price)

        
        


        


        

    
    return render_template("index.html",brand=brand,Type=Type,Inches=Inches,Resolution=Resolution,Ram=Ram,OpSys=OpSys,Weight=Weight,Touchscreen=Touchscreen,Ips_Panel=Ips_Panel,Ghz=Ghz,Processor_Name=Processor_Name,Processor_Generation=Processor_Generation,Storage_type=Storage_type,Storage_Size=Storage_Size,Gpu_Brand=Gpu_Brand,Gpu_Name=Gpu_Name)


app.run(debug=True)