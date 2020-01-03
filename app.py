from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/temperature', methods=['POST'])
def temperature():
    zipcode = request.form['zip']
    r = requests.get(
        'https://api.openweathermap.org/data/2.5/weather?zip=' + zipcode + ',in&appid=ba7bb2fcd4d0e41b8155727a76289e9f')
    jsonobj = r.json()
    z = jsonobj['main']['temp']
    temp_k = float(jsonobj['main']['temp'])
    temp_c = temp_k - 273.15
    temp_c = "{0:.2f}".format(temp_c)
    return render_template('temperature.html', temp=temp_c, zipcode=zipcode)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
