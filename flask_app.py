from flask import Flask, redirect, render_template, url_for
import math
import socket
import threading
import time
import requests

app = Flask(__name__)

headers = {
     'Metadata': 'true',
}

params = (
    ('api-version', '2020-10-01'),
)

hostname = socket.gethostname()

keepstressing = False

def stresserthread():
    while (True):
        while (keepstressing == True):
            for x in range(1, 69):
                math.factorial(x)
        time.sleep(3)

stresser_thread = threading.Thread(target=stresserthread, args=())
stresser_thread.start()



@app.route("/")
def root():
    return render_template('stress.html', hostname=hostname, keepstressing=keepstressing)

@app.route("/start_stress")
def start_stress():
    global keepstressing
    keepstressing = True
    return redirect(url_for('root'))

@app.route("/stop_stress")
def stop_stress():
    global keepstressing
    keepstressing = False
    return redirect(url_for('root'))

if __name__ == "__main__":
    app.run()