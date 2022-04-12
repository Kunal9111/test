from flask import Flask

app = Flask(__name__)
@app.route("/<name>")
def print_name(name):
    return f"Welcome {name}" 

if __name__ == "_main_":
    app.run(host = '0.0.0.0', port = 9000, debug = True)
    