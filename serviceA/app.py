from flask import Flask
import os
import requests
import json
import _thread
from flask import render_template
from flask import jsonify
from ScheduledRate import ScheduledRate
app = Flask(__name__)

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

def getBitInDolar():
    res = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = res.json()
    rate = data['bpi']['USD']['rate_float']
    return rate

runn = ScheduledRate(10,getBitInDolar)
_thread.start_new_thread(runn.scheule_a_job,(60,))


def getAVGCoinRete():
    return str(runn.calcAVGCoinRete())

@app.route("/")
def index():
 try:
    return render_template("index.html",AVG_Rate = getAVGCoinRete(),rateNow=getBitInDolar(),coin ="Dollar")
 except Exception as e:
    print(e)  
    html = "<h3>An error occurred while connecting to the server. Please contact your service provider </h3>" 
    return html


if __name__ == "__main__": 
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False,host='0.0.0.0',port=port)
