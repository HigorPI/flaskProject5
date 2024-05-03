from flask import Flask, render_template

app = Flask(__name__)

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Página de prevenção
@app.route('/prevencao')
def prevencao():
    return render_template('prevencao.html')

if __name__ == '__main__':
    app.run(debug=True)

