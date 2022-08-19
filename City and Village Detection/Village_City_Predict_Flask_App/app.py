import re
from flask import Flask,render_template,request
import cv2
import numpy as np
import os
from werkzeug.utils import secure_filename
from keras.models import load_model

model = load_model('model.h5')

app = Flask(__name__)


app.config['IMAGE_UPLOAD'] = 'F:/Flask_APP/Village City predict/static/images'

@app.route('/', methods =["GET", "POST"])
def home():
    if request.method == "POST":
        img = request.files['file']

        filename = secure_filename(img.filename)
        filepath = os.path.join(app.config['IMAGE_UPLOAD'], filename)
        img.save(filepath)
       
        read_img = cv2.imread(filepath)
        shape_img = cv2.resize(read_img,(30,30))
        ar_img = np.array(shape_img)
        bks = ar_img.reshape(1,30,30,3)
        data = model.predict(bks)[0][0]

        if(data >= float(0.8)):
            data="City"
        else:
            data = "Village"
        
        return render_template("index.html",data=data)
    return render_template("index.html")


app.run(debug=True)