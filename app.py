import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

# Define a rota da página inicial
@app.route('/')
def index():
    # Lê os dados do arquivo CSV
    df = pd.read_csv('dados.csv')
    # Converte os dados para uma lista de dicionários
    data = df.to_dict('records')
    # Renderiza o template HTML com os dados
    return render_template('index.html', data=data)

if __name__ == '__main__':
    # Executa o servidor na porta 5000
    app.run(port=5000)
