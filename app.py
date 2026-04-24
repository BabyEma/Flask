from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pagina1')
def pagina1():
    nombres = ["Juan", "Ana", "Luis"]
    return render_template('pagina1.html', nombres=nombres)

@app.route('/pagina2')
def pagina2():
    usuarios = [
        {"nombre": "Carlos", "edad": 20},
        {"nombre": "María", "edad": 25}
    ]
    return render_template('pagina2.html', usuarios=usuarios)

if __name__ == '__main__':
    app.run(debug=True)
    