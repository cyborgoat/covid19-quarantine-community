import collections
import datetime
import json
import pathlib
from collections import OrderedDict, defaultdict

import numpy as np
import requests
import pandas as pd
from requests.auth import HTTPBasicAuth
from xlsxwriter import workbook

from excel.formatter import format

today = datetime.date.today()
end_date = datetime.date.today() - datetime.timedelta(days=1)

DEBUG = False
api_url = "http://121.43.36.132/api/" if not DEBUG else "http://127.0.0.1:8000/api/"

supply_request_url = api_url + 'supply_requests/'
drinking_water_request_url = api_url + 'drinking_water_requests/'
special_request_url = api_url + 'special_requests/'

with open(pathlib.Path(__file__).parent.joinpath('credentials.json'), 'r') as f:
    credentials = json.load(f)

with open(pathlib.Path(__file__).parent.joinpath('word_dict.txt'), 'r') as f:
    word_dict = OrderedDict()
    lines = f.readlines()
    for line in lines:
        words = line.strip().split(' ')
        word_dict[words[0]] = words[1]


def get_water_df() -> pd.DataFrame:
    response = requests.get(drinking_water_request_url,
                            auth=HTTPBasicAuth(credentials['name'], credentials['password']))
    js = response.json()['results']
    df = pd.DataFrame.from_dict(js)
    df['created_on'] = pd.to_datetime(df['created_on'])
    df['date'] = df['created_on'].map(datetime.datetime.date)
    df = df.loc[df['date'] == today]
    df['created_on'] = df['created_on'].dt.strftime('%H:%M:%S')
    df.drop(['resolved'], axis=1, inplace=True)
    ordered_list = [i for i in word_dict if i in df.columns]
    df = df[ordered_list]
    df.columns = [word_dict[i] for i in df.columns]
    # print(df)
    return df


def water_stat_table():
    df = get_water_df()
    df = df.sort_values(by=['院号', '楼号', '单元号', '房间号'], ascending=True)
    total_needed = len(df)
    tmp_res = collections.OrderedDict()
    maxlen = 0
    for row in df.to_dict(orient='records'):
        print(row)
        unit_name = "" if str(row['单元号']).startswith('0') else f"{row['单元号'].replace('单元', '-')}"
        building = f"{row['院号']}-{row['楼号']}"
        if building not in tmp_res.keys():
            tmp_res[building] = []
        tmp_res[building].append(f"{unit_name}{row['房间号']}")
        maxlen = max(maxlen, len(tmp_res[building]))
    cols = len(tmp_res.keys())
    rows = maxlen
    matrix = [[''] * cols for _ in range(rows + 1)]
    for i, (key, vals) in enumerate(tmp_res.items()):
        matrix[0][i] = f"共{len(vals)}箱"
        for j, val in enumerate(vals):
            matrix[j + 1][i] = val

    ret_df = pd.DataFrame(data=matrix, columns=tmp_res.keys())
    out_path = pathlib.Path('data', f'瓶装水需求-{today}.xlsx')

    writer = pd.ExcelWriter(out_path, engine='xlsxwriter')
    ret_df.to_excel(writer, sheet_name='瓶装水统计', index=False, na_rep='NaN')

    cell_format = workbook.Format({'bold': True, 'font_color': 'red'})

    # Auto-adjust columns' width
    for column in ret_df:
        column_width = 18
        col_idx = ret_df.columns.get_loc(column)
        writer.sheets['瓶装水统计'].set_column(col_idx, col_idx, column_width)

    writer.save()
    # ret_df.to_excel(out_path, index=False)
    # format(out_path)
    # ret_df.to_csv(out_path)


def api2df(url, file_title: str, write: bool = True, multi_req=True):
    response = requests.get(url, auth=HTTPBasicAuth(credentials['name'], credentials['password']))
    js = response.json()['results']
    df = pd.DataFrame.from_dict(js)
    if len(df) > 0:
        df['created_on'] = pd.to_datetime(df['created_on'])
        df['date'] = df['created_on'].map(datetime.datetime.date)
        df['created_on'] = df['created_on'].dt.strftime('%H:%M:%S')
        df = df.loc[df['date'] == today]

        if multi_req:
            df['items'] = df['items'].apply(lambda x: ','.join(x))

        ordered_list = [i for i in word_dict if i in df.columns]
        df = df[ordered_list]
    df.columns = [word_dict[i] for i in df.columns]
    print(df)
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
    # supply_df = api2df(supply_request_url, '必需品需求', write=False, multi_req=True)
    # supply_df = api2df(drinking_water_request_url, '瓶装水需求', write=False, multi_req=False)
    # special_df = api2df(special_request_url, '特殊需求')
    # do_supply_static(supply_df)
    water_stat_table()
