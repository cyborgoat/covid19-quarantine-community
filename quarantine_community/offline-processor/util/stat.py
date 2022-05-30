import datetime
import json
import pathlib
from collections import OrderedDict, defaultdict

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

with open(pathlib.Path(__file__).parent.joinpath('credentials.json'), 'r') as f:
    credentials = json.load(f)

with open(pathlib.Path(__file__).parent.joinpath('word_dict.txt'), 'r') as f:
    word_dict = OrderedDict()
    lines = f.readlines()
    for line in lines:
        words = line.strip().split(' ')
        word_dict[words[0]] = words[1]


def api2df(url, file_title: str, write: bool = True, special_req=False):
    response = requests.get(url, auth=HTTPBasicAuth(credentials['name'], credentials['password']))
    js = response.json()['results']
    df = pd.DataFrame.from_dict(js)
    if len(df) > 0:
        df['created_on'] = pd.to_datetime(df['created_on'])
        df['date'] = df['created_on'].map(datetime.datetime.date)
        df['created_on'] = df['created_on'].dt.strftime('%H:%M:%S')
        df = df.loc[df['date'] == today]

        if not special_req:
            df['items'] = df['items'].apply(lambda x: ','.join(x))

        ordered_list = [i for i in word_dict if i in df.columns]
        df = df[ordered_list]
    df.columns = [word_dict[i] for i in df.columns]

    if write:
        df.to_excel(pathlib.Path('data', f'{file_title}-{today}.xlsx'), index=False)

    return df


def do_supply_static(df: pd.DataFrame, file_title: str, write: bool = True, special_req=False):
    res = {}
    key1, key2, key3, key4 = ['院号', '楼号', '单元号', '物品']
    if special_req:
        key4 = ['详情']

    for row in df.to_dict(orient='records'):
        country_yard = row[key1]
        building_unit = row[key2]
        building_subunit = row[key3]
        items = row[key4]
        if country_yard not in res.keys():
            res[country_yard] = {}
        if row[key2] not in res[country_yard].keys():
            res[country_yard][building_unit] = {}
        if row[key3] not in res[country_yard][building_unit].keys():
            res[country_yard][building_unit][building_subunit] = defaultdict(int)
        for i in items.split(','):
            res[country_yard][building_unit][building_subunit][i] += 1

    ret = []
    for i_key, i_val in res.items():
        for j_key, j_val in i_val.items():
            for k_key, k_val in j_val.items():
                ret.append([i_key, j_key, k_key, dict(k_val)])
    ret_df = pd.DataFrame(data=ret, columns=[key1, key2, key3, key4])
    ret_df = ret_df.sort_values([key1, key2, key3], ascending=[True, True, True])
    if write:
        ret_df.to_excel(pathlib.Path('data', f'{file_title}-综合统计-{today}.xlsx'), index=False)
    return ret_df


if __name__ == '__main__':
    supply_df = api2df(supply_registration_url, '必需品需求', write=False)
    # special_df = api2df(special_request_url, '特殊需求')
    # do_supply_static(supply_df)
