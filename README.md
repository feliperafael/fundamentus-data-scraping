# Fundamentus Data Scraping

Esse repositório tem o objetivo de extrair dados fundamentalistas de ações da bolsa brasileira a partir do site [Fundamentus](http://www.fundamentus.com.br/detalhes.php). 

## Dados Extraídos

O script `script.py` extrai os seguintes dados para o ativo especificado:

- Indicadores fundamentalistas 
- Balanço Patrimonial
- Demonstrativo de Resultados

Os dados são extraídos da página de detalhes do ativo no Fundamentus.

## Configurando o Ambiente

É recomendado usar um ambiente virtual para isolar as dependências deste projeto. Para criar e ativar um ambiente virtual:

```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
source venv/bin/activate  # No Linux
venv\Scripts\activate     # No Windows
```

Depois de ativar o ambiente virtual, instale as dependências com:

```bash
pip install -r requirements.txt
```

## Dependências

As dependências do projeto estão listadas no arquivo `requirements.txt`:

- beautifulsoup4==4.11.2
- pandas==1.5.3
- requests==2.28.2

Instale todas as dependências de uma vez usando `pip install -r requirements.txt` (de preferência dentro do seu ambiente virtual).

## Como Usar

Para extrair os dados de um ativo, rode o script passando o código do ativo como argumento:

```
python script.py CODIGO_DO_ATIVO
```

Por exemplo, para o ativo ABEV3:

```
python script.py ABEV3
```

Os dados extraídos serão salvos na pasta `output` em dois formatos:

- `CODIGO_DO_ATIVO.json`: Dados brutos em formato JSON
- `CODIGO_DO_ATIVO.csv`: Dados em formato CSV para fácil análise


## Roadmap

Aqui estão alguns planos e ideias para melhorias futuras deste projeto:

- Integração com modelos de linguagem (LLMs) como OpenAI, Groq e DeepSeek para gerar agentes que possam analisar os dados fundamentalistas extraídos e sugerir boas opções de investimento.

- Geração de gráficos e relatórios a partir dos dados extraídos para facilitar a visualização e análise das informações fundamentalistas.

- Adição de funcionalidade para comparar os dados fundamentalistas do ativo especificado com outros papéis de categoria similar, fornecendo mais contexto para a análise.

- Aprimoramento do script para coletar dados históricos e acompanhar a evolução dos indicadores fundamentalistas ao longo do tempo.

- Criação de uma interface web amigável para permitir que usuários menos técnicos possam facilmente extrair e analisar dados fundamentalistas.

- Expansão da cobertura para incluir ações de outras bolsas além da B3, como bolsas internacionais.

Sinta-se à vontade para abrir issues ou pull requests se tiver sugestões ou quiser contribuir com esses planos!


## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.
