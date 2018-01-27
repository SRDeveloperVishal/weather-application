import requests
import psycopg2
import psycopg2.extras
from datetime import datetime
import logging


def fetch_data():
    api_token = 'bb3d7329b8e3cbb0'

    url = 'http://api.wunderground.com/api/' + api_token + '/conditions/q/India/Delhi.json'
    r = requests.get(url).json()
    data = r['current_observation']

    location = data['observation_location']['full']
    weather = data['weather']
    wind_str = data['wind_string']
    temp = data['temp_c']
    humidity = data['relative_humidity']
    precip = data['precip_today_string']
    icon_url = data['icon_url']
    observation_time = data['observation_time']

    try:
        conn = psycopg2.connect(dbname='df3m11t651heh7', user='htjqovxutdowtg', host='ec2-54-225-230-142.compute-1.amazonaws.com', password='2066ad4ab7270ea37e686fa0f97b7bf3516927f43adce742fb66e709a3847e45')
        print('connected to DB successfully')
    except:
        print(datetime.now(), "unable to connect to database")
        logging.exception("unable to open the database")
        return
    else:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cur.execute("""INSERT INTO weatherstation_reading(location, weather, wind_str, temp, humidity, precip, icon_url, observation_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""", (location, weather, wind_str, temp, humidity, precip, icon_url,observation_time))

    conn.commit()
    cur.close()
    conn.close()

    print("Data Written", datetime.now())

fetch_data()