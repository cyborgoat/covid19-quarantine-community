import datetime
import json
import pathlib

import numpy as np
import requests
import pandas as pd
from requests.auth import HTTPBasicAuth

today = datetime.date.today()
end_date = datetime.date.today() - datetime.timedelta(days=1)

DEBUG = False
api_url = "http://121.43.36.132/api/" if not DEBUG else "http://127.0.0.0:8000/api/"

supply_registration_url = api_url + 'supply_registration/'
special_request_url = api_url + 'special_requests/'

with open('credentials.json', 'r') as f:
    credentials = json.load(f)

with open('word_dict.txt', 'r') as f:
    word_dict = dict()
    lines = f.readlines()
    for line in lines:
        words = line.strip().split(' ')
        word_dict[words[0]] = words[1]


def api2df(url, file_title: str, write: bool = True):
    response = requests.get(url, auth=HTTPBasicAuth(credentials['name'], credentials['password']))
    js = response.json()['results']
    df = pd.DataFrame.from_dict(js)
    if len(df) > 0:
        df['created_on'] = pd.to_datetime(df['created_on']).map(datetime.datetime.date)
        df = df.loc[df['created_on'] == today]
    df.columns = [word_dict[i] for i in df.columns]

    if write:
        df.to_excel(pathlib.Path('data', f'{file_title}-{today}.xlsx'))

    return df


if __name__ == '__main__':
    supply_df = api2df(supply_registration_url, '必需品需求')
    special_df = api2df(special_request_url, '特殊需求')
