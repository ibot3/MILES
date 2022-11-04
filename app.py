from flask import redirect, url_for, render_template, abort, send_from_directory, send_file, jsonify, request
from flask import Flask

from gevent.pywsgi import WSGIServer
import threading
import random
import json
import time
import os
import io
import sys
import getopt

from simplifier import simplifier
from simplifier import models
from simplifier import config

#Create app
app = Flask(__name__,static_url_path='')
app.debug = False

@app.route('/')
def index(): 
    return render_template('index.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/ai_request/', methods=['GET', 'POST'])
def ai_request():
    
    if request.method == 'POST':
        text = request.form.get('input')
        output = simplifier.simplify_text(text, bold_highlight=True)
        return jsonify({"output": output})


if __name__ == "__main__":

    if len(sys.argv) > 1:
        
        argv = sys.argv[1:]

        try:
            opts, args = getopt.getopt(argv, "l:")
        except:
            print("Error!")

        # Get language if passed.
        for opt, arg in opts:
            if opt in ['-l', '--language']:
                config.lang = arg

    # Check if language is supported and attempt to load embeddings.
    if config.lang in config.supported_langs:
        models.embeddings = models.load_embeddings(config.lang)

    print("\nStarting MILES Flask server...")
    http_server = WSGIServer(('0.0.0.0', 8080), app)    
    print("\nLoaded as HTTP Server on port 8080, running forever:")
    http_server.serve_forever()
