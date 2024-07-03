#~ USAGE
# cd d:\python_developer
# .\pydev\Scripts\activate
# cd d:\python_developer\lesson_01
#~~~~~~~~~~~~~~~~~~~~~~~~
# python main.py
#~~~~~~~~~~~~~~~~~~~~~~~~  


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import requests
import json
from flask import Flask

import datetime

def get_valutes_list():
  url = 'https://www.cbr-xml-daily.ru/daily_json.js'
  response = requests.get(url)
  data = json.loads(response.text)
  valutes = list(data['Valute'].values())
  return valutes


app = Flask(__name__)


def create_html(valutes):
  event_datetime = datetime.datetime.now()
  text = f'<h1>Курс валют. Дата и время:  {event_datetime.strftime("%Y.%m.%d %H:%M:%S")}</h1>'
  text += '<table>'
  text += '<tr>'
  for _ in valutes[0]:
    text += f'<th><th>'
  text += '</tr>'
  for valute in valutes:
    text += '<tr>'
    for v in valute.values():
      text += f'<td>{v}</td>'
    text += '</tr>'

  text += '</table>'
  return text


@app.route("/")
def index():
  valutes = get_valutes_list()
  html = create_html(valutes)
  return html


if __name__ == "__main__":
  app.run()
