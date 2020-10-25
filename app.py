from __future__ import unicode_literals
import json
import logging
from flask import Flask, request

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return '<h1>ghb</h1>'

@app.route('/privet', metods=['POST'])
def main():
    response = {
    'version': request.json['version'],
    'session': request.json['session'],
    'response': {
        'end_session': False,
        'text': "Ну привет!"
        }
    }

    logging.info('Response: %r', response)

    return json.dumps(response, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    app.run()
