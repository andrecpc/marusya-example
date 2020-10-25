from __future__ import unicode_literals
import json
import logging
from flask import Flask, request

app = Flask(__name__)
app.debug = True

# @app.route('/')
# def index():
#     return '<h1>ghb</h1>'

@app.route('/marusya', methods=['POST', 'GET'])
def marusya():
    return "Marusya"

@app.route('/privet', methods=['POST'])
def main():

    card = {}
    buttons = {}

    if request.json['session']['new']:
        text = 'Это еще тестовый навык'




    response = {
    'version': request.json['version'],
    'session': request.json['session'],
    'response': {
        'end_session': False,
        'text': text,
        'card': card,
        'buttons': buttons
        }
    }

    logging.info('Response: %r', response)

    return json.dumps(response, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    app.run()
