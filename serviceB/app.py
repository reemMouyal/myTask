from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route("/")
def hello():
 try:
    html = "<h3>Hi, {name}!</h3>" 
    return html.format(name="Service B Is Running")
 except Exception as e:
    print(e)
    html = "<h3>An error occurred while connecting to the server. Please contact your service provider </h3>" 

@app.route("/ready")
def ready():
    resp = jsonify(success=True)
    resp.status_code = 200
    return resp

@app.route("/alive")
def alive():
    resp = jsonify(success=True)
    resp.status_code = 200
    return resp
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)