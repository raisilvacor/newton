import json
import os
import urllib.parse
from jinja2 import Environment, FileSystemLoader

def build():
    # Carregar dados
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Configurar Jinja2
    env = Environment(loader=FileSystemLoader('.'))
    
    # Adicionar filtro urlencode
    env.filters['urlencode'] = urllib.parse.quote
    
    template = env.get_template('index_template.html')
    
    # Renderizar
    output = template.render(**data)
    
    # Salvar index.html
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(output)
    
    print("Site buildado com sucesso em index.html")

if __name__ == "__main__":
    build()
