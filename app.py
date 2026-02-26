from flask import Flask, render_template, send_from_directory
import json
import os
import urllib.parse

app = Flask(__name__, template_folder='.')

# Adicionar filtro urlencode para o Jinja2 no Flask
@app.template_filter('urlencode')
def urlencode_filter(s):
    if s is None:
        return ""
    return urllib.parse.quote(s)

def load_data():
    with open('data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def index():
    # Se o index.html existir (foi buildado), servimos ele.
    # Caso contrário, renderizamos on-the-fly do template.
    if os.path.exists('index.html'):
        return send_from_directory('.', 'index.html')
    
    data = load_data()
    return render_template('index_template.html', **data)

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    print(f"Servidor rodando em http://localhost:{port}")
    app.run(host='0.0.0.0', port=port, debug=True)
