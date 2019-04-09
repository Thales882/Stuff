import requests
from flask import Flask, render_template, url_for

import sqlalchemy

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
@app.route('/weather')
def tempo():
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=4f3cb39756ebaab292212f26be6c7a22'
    city = 'Brasília'

    r = requests.get(url.format(city)).json()
    

    weather = {
        'city'        : city ,
        'temperature' : r['main']['temp'],
        'description' : r['weather'][0]['description'],
        'icon'        : r['weather'][0]['icon']
    }
    translate = {
        'nublado' : r['weather'][0]['description']
    }
    print(translate)
    print(weather)


    return render_template('weather.html', weather=weather, translate=translate, title='Brasília')



if __name__=="__main__":
    app.run()