from flask import Flask, request
from flasgger import Swagger
import pickle
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)
Swagger(app)

pickled_model = open("pickle_diabetes_model.pkl","rb")
classifier = pickle.load(pickled_model)

@app.route('/')  #decorators
def home():
    return "welcome to my model"

@app.route('/predict')
def predict_diabetes():

    """Lets try Swagger from flasgger
    ---
    parameters:
        - name: age
          in: query
          type: number
          required: true  
        - name: sex
          in: query
          type: number
          required: true
        - name: bmi
          in: query
          type: number
          required: true
        - name: bp
          in: query
          type: number
          required: true
        - name: s1
          in: query
          type: number
          required: true
        - name: s2
          in: query
          type: number
          required: true
        - name: s3
          in: query
          type: number
          required: true
        - name: s4
          in: query
          type: number
          required: true
        - name: s5
          in: query
          type: number
          required: true
        - name: s6
          in: query
          type: number
          required: true


    responses:
        200:
            description: The result is    
    """

    a = request.args.get("age")
    b = request.args.get("sex")
    c = request.args.get("bmi")
    d = request.args.get("s1")
    e = request.args.get("s2")
    f = request.args.get("s3")
    g = request.args.get("s4")
    h = request.args.get("s5")
    i = request.args.get("s6")

    result = classifier.predict([[a,b,c,d,e,f,g,h,i]])

    return f"The diabetes prediction is{result}"

if __name__ == "__main__":
    app.run()