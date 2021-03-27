from flask import Flask, render_template
import requests
import pprint
import time 

app = Flask(__name__)

def fetch_data():
    
    
    api = 'http://api.open-notify.org/iss-now.json'
    
    req = requests.get(api)
    json = req.json()
    
    latitude = json['iss_position']['latitude']
    longitude = json['iss_position']['longitude']
    
    time.sleep(5)
    
    
    return (latitude, longitude)
    

    


@app.route('/')
def main():
    
        
    iss = fetch_data()

    lat = iss[0]
    lon = iss[1]
    
    print(lat, lon)


    return render_template('iss.html', lat = lat, lon = lon)


if __name__ == '__main__':
    app.run(debug = True)