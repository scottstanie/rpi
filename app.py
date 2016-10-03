from __future__ import unicode_literals
import os
from flask import Flask, render_template, request, jsonify
import json, requests


RESULTS_PER_PAGE = 10
# configuration
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    host = os.environ.get("HOST", '0.0.0.0')
    app.run(host=host, port=port)
