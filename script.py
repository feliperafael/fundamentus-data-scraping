#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:45:31 2019

@author: felipe
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys


def get_raw_data(url):    
    r = requests.get(url)
    r.encoding = 'utf-8'
    return r.content


def build_url(papel):
    url_base = 'http://www.fundamentus.com.br/detalhes.php?papel={}'.format(papel)
    return url_base

def parse_html(html):
    soup = BeautifulSoup(html)
    tables = soup.findAll("table")
    
    df = pd.read_html(str(tables).replace('?', ''))
    return df

if __name__ == "__main__":
    papeis = [str(sys.argv[1])]
    
    for papel in papeis:
        url = build_url(papel)
        html = get_raw_data(url)
        dfs = parse_html(html)
        df_final = pd.DataFrame()
        
        for df in dfs:
            df_final = df_final.append(df)
        df_final.to_csv('output/{}.csv'.format(papel), index=False, header=False)