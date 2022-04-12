from flask import Flask

app = Flask(__name__)
@app.route("/<name>")
def print_name(name):
    return f"Welcome {name}" 

if __name__ == "_main_":
    app.run()
    