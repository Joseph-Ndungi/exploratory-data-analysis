import requests
import pandas as pd


url= 'https://randomuser.me/api/'

params = {
    'results': 100,
    'gender': 'male'
}

response = requests.get(url, params=params)

data = response.json()

#df = pd.DataFrame(columns=['gender', 'name'])

#convert json to dataframe
df = pd.json_normalize(data['results'])


