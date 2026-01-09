from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    titulo= "IDGS-802-Flask"
    lista = ['juan','diego']
    return render_template('index.html', titulo=titulo, lista=lista)

@app.route('/formulario')
def formulario():

    return render_template('formularios.html')

@app.route('/index')
def reportes():
    return render_template('reportes.html')

@app.route('/hola')
def about():
    return 'Hola, Hola!'


@app.route('/user/<nombre>')
def user(nombre):
    return f'Hola, {nombre}!'

@app.route('/numero/<int:n>')
def numero(n):
    return f'Numero, {n}!'



@app.route('/user/<id>/<username>')
def username(id, username):
    return f'Hola, {username} con id {id}!'

@app.route('/suma/<n1>/<n2>')
def suma(n1, n2):
    return 'La suma es {}'.format(float(n1) + float(n2))

@app.route("/default")
@app.route("/default/<nombre>")
def default(nombre="juan"):
    return f"Hola {nombre}"

@app.route("/operas")
def operas():
    return '''
    <form>
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>
    
    <label for="name">Apaterno:</label>
    <input type="text" id="apaterno" name="apaterno" required>
    </form>
'''

if __name__ == '__main__':
    app.run(debug=True)