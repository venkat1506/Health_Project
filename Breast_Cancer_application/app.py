from flask import Flask, render_template, url_for, flash, redirect
import joblib
from flask import request
import numpy as np
import os
from flask_cors import  cross_origin

app = Flask(__name__, template_folder='templates')

@app.route("/")

@app.route("/cancer")
@cross_origin()
def cancer():
    return render_template("cancer.html")

def ValuePredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==5):
        loaded_model = joblib.load(r'./../Model/BreastCance_model.pkl')
        result = loaded_model.predict(to_predict)
    return result[0]

@app.route('/predict', methods = ["POST"])
def predict():
    if request.method == "POST":
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
         #cancer
        if(len(to_predict_list)==5):
            result = ValuePredictor(to_predict_list,5)
    
    if(int(result)==1):
        prediction = "Sorry you chances of getting the disease. Please consult the doctor immediately"
    else:
        prediction = "No need to fear. You have no dangerous symptoms of the disease"
    return(render_template("result.html", prediction_text=prediction))       

if __name__ == "__main__":
    # port = int(os.environ.get("PORT", 7000))
    # app.run(host='localhost', port=port)

    app.run(host='0.0.0.0', port=12345)
    # app.run(debug=True)
