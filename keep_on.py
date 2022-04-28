from flask import Flask
from threading import Thread

app = Flask('')
def home():
    return "Web server still on"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_on():
    t = Thread(target=run)
    t.start()