from flask import Flask
from threading import Thread
import time
from CommitMaker import main


app = Flask("")

@app.route("/")
def home():
    return "Web server still on"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_on():
    t = Thread(target=run)
    t.start()
    while 1:
        #time.sleep(86400)
        main()
        print("\n\ncommitMade")

keep_on()