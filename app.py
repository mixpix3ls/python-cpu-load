from flask import Flask, redirect, render_template, url_for
import math
import socket
import threading
import time
import requests


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

application = Flask(__name__)

@application.route("/")
def root():
    return render_template('stress.html', hostname=hostname, keepstressing=keepstressing)

@application.route("/start_stress")
def start_stress():
    global keepstressing
    keepstressing = True
    return redirect(url_for('root'))

@application.route("/stop_stress")
def stop_stress():
    global keepstressing
    keepstressing = False
    return redirect(url_for('root'))

if __name__ == "__main__":
    application.run(host='0.0.0.0', port = 8080)
