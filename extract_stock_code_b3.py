import requests
from bs4 import BeautifulSoup
import json
import chardet
import os
import argparse

def get_b3_stock_codes():
    url = "https://www.fundamentus.com.br/detalhes.php"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    response = requests.get(url, headers=headers)
    
    # Detectar a codificação correta
    detected_encoding = chardet.detect(response.content)['encoding']
    response.encoding = detected_encoding if detected_encoding else 'utf-8'
    
    if response.status_code != 200:
        raise Exception(f"Falha ao acessar {url}. Código de status: {response.status_code}")
        
    soup = BeautifulSoup(response.text, 'lxml')  # Usar lxml como parser
    
    table = soup.find('table', {'id': 'test1', 'class': 'resultado'})

    if table is None:
        raise Exception("Tabela com os códigos de ações não encontrada na página.")

    stock_codes = []

    for row in table.find_all('tr')[1:]:  # Pula a primeira linha do cabeçalho
        cells = row.find_all('td')
        if len(cells) >= 3:
            stock_code = cells[0].text.strip()
            company_name = cells[1].text.strip()
            company_full_name = cells[2].text.strip()
            
            if stock_code and company_name and company_full_name:
                stock_data = {
                    'codigo': stock_code,
                    'nome': company_name,
                    'razao_social': company_full_name
                }
                stock_codes.append(stock_data)
            
    return stock_codes

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extrair códigos de ações da B3.")
    parser.add_argument('--no-cache', action='store_true', help='Ignorar cache e baixar novamente os dados.')
    args = parser.parse_args()

    file_path = os.path.join("data", "b3_stock_codes.json")
    
    if args.no_cache or not os.path.exists(file_path):
        stock_codes = get_b3_stock_codes()
        
        print(f"Total de {len(stock_codes)} ações encontradas na B3.")
        
        os.makedirs("data", exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(stock_codes, f, ensure_ascii=False, indent=2)
    else:
        print(f"O arquivo {file_path} já existe. Nenhuma extração realizada.")
