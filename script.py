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
from io import StringIO
import json


def get_raw_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    if r.status_code != 200:
        raise Exception(f"Failed to retrieve data from {url}, status code: {r.status_code}")
    return r.content


def build_url(papel):
    url_base = 'http://www.fundamentus.com.br/detalhes.php?papel={}'.format(papel)
    return url_base

def parse_html(html):
    print(html)
    soup = BeautifulSoup(html, features="lxml")
    print(soup)
    tables = soup.findAll("table")
    
    if not tables:
        raise ValueError("No tables found in the HTML content.")
    
    # Use StringIO to wrap the string
    df = pd.read_html(StringIO(str(tables).replace('?', '')), decimal=',', thousands='.')
    return df


def csv_to_json(file_path) -> str:
    """
    Converte um arquivo CSV em uma string JSON.

    Lê um arquivo CSV em um DataFrame, remove linhas vazias e converte os dados em um dicionário,
    onde as chaves e valores são extraídos de colunas alternadas. O dicionário é então convertido
    em uma string JSON formatada.

    Args:
        file_path (str): O caminho para o arquivo CSV a ser lido.

    Returns:
        str: A representação em string JSON dos dados do arquivo CSV.
    """
    df = pd.read_csv(file_path, header=None)
    df.dropna(how='all', inplace=True)
    json_data = {}
    
    for i in range(0, df.shape[1], 2):
        keys = df.iloc[:, i]
        values = df.iloc[:, i + 1]
        
        for key, value in zip(keys, values):
            if pd.notna(key) and pd.notna(value):
                json_data[key] = value
    
    json_str = json.dumps(json_data, ensure_ascii=False, indent=4)
    
    return json_str


if __name__ == "__main__":
    papeis = [str(sys.argv[1])]
    
    for papel in papeis:
        url = build_url(papel)
        html = get_raw_data(url)
        dfs = parse_html(html)
        df_final = pd.concat(dfs, ignore_index=True)
        
        df_final.to_csv('output/{}.csv'.format(papel), index=False, header=False)

    # Exemplo de uso
    file_path = 'output/ABEV3.csv'
    json_output = csv_to_json(file_path)
    with open('output/{}.json'.format(papel), 'w', encoding='utf-8') as json_file:
        json_file.write(json_output)
    print(json_output)
