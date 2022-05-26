from flask import Flask
from threading import Thread

#Se usa flask como el web server
app = Flask('')

@app.route('/')
def home():
    return "No estaba muerto, andaba de parranda"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()