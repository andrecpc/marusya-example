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
    buttons = []
    end_session = False
    text = ''

    if request.json['session']['new']:
        text = 'Это еще тестовый навык'
    elif request.json['request']['command'].lower() == 'привет':
        text = 'Привет!!!'
    elif request.json['request']['command'].lower() == 'хватит':
        text = 'Хорошо, до встречи!'
        end_session = True
    elif request.json['request']['command'].lower() == 'картинка':
        text = 'Вот такая есть картинка:'
        card = {
            'type': 'BigImage',
            'image_id': 457239018,
            'title': 'Это Коржик — офисный пёс',
            'description': ''
                }
    elif request.json['request']['command'].lower() == 'кнопки':
        text = 'Вот такие есть кнопки:'
        buttons = [
                    {'title': 'кнопка 1'},
                    {'title': 'кнопка 2'}
                  ]
    elif request.json['request']['command'].lower() == 'карусель':
        text = 'Карусель:'
        card = {
            "type": "ItemsList",
            "title": "Две картинки",
            "description": "",
            "items": [{"image_id": 457239018}, {"image_id": 457239017}]
                }
    else:
        text = request.json['request']['command'].lower()

    response = {
    'version': request.json['version'],
    'session': request.json['session'],
    'response': {
        'end_session': end_session,
        'text': text,
        'card': card,
        'buttons': buttons
        }
    }

    logging.info('Response: %r', response)

    return json.dumps(response, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    app.run()
