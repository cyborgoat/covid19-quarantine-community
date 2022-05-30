import datetime
import json

import requests
import pandas as pd
from requests.auth import HTTPBasicAuth

start_date = datetime.date.today()
end_date = datetime.date.today()

print(start_date,end_date)
exit()

with open('credentials.json', 'r') as f:
    credentials = json.load(f)


def api2df(url):
    response = requests.get(url, auth=HTTPBasicAuth(credentials['name'], credentials['password']))
    js = response.json()['results']
    df = pd.DataFrame.from_dict(js)
    if len(df) > 0:
        df['created_on'] = (df['created_on'])
    return df


DEBUG = False
api_url = "http://121.43.36.132/api/" if not DEBUG else "http://127.0.0.0:8000/api/"

supply_registration_url = api_url + 'supply_registration/'
special_request_url = api_url + 'special_requests/'

supply_df = api2df(supply_registration_url)
special_df = api2df(special_request_url)

print(supply_df)
print(special_df)
