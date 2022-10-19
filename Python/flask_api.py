from flask import Flask
import requests
import json

app=Flask(__name__)


@app.route('/',methods = ['get'])
def home(): 
    url = 'https://random-data-api.com/api/address/random_address'
    data = requests.get(url= url).json()
    return json.dumps(data) 
    


if __name__ == '__main__':
    app.run(debug=True)

