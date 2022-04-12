
from flask import Flask, request
from flasgger import Swagger

app = Flask(__name__) #constructor of the flask
Swagger(app)

@app.route('/')
def base_route():
    return "Welcome to Praxis"

@app.route("/my_name/<name>")
def print_name(name):
    return f"Happy Leaning {name} in Praxis BLR" 

@app.route("/hello", methods = ["GET","POST"])
def hello():

    """Lets try the Swagger from Flasgger
    ---
    parameters: 
        - name: StudentName
          in: query
          type: string
          required: true
        - name: RollNumber
          in: query
          type: string
          required: true
    responses: 
        200: 
            description: The result is
    """
    stu_name = request.args.get("StudentName")
    numb = request.args.get("RollNumber")
    return f"Studnet name is {stu_name} and Roll number is {numb}"

if __name__ == "__main__":
    app.run(debug = True)

