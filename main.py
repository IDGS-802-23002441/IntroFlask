from wtforms.validators import email
from flask import Flask, render_template, request
from flask import flash
from flask_wtf.csrf import CSRFProtect

import forms


app = Flask(__name__)
app.secret_key = 'clave secreta'
csrf = CSRFProtect()


@app.route('/')
def index():
    titulo= "IDGS-802-Flask"
    lista = ['juan','diego']
    return render_template('index.html', titulo=titulo, lista=lista)

@app.route('/formulario')
def formulario():
    return render_template('formularios.html')


@app.route('/reporte')
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


@app.route('/operasBas', methods=["GET", "POST"])
def operas1():
    n1, n2, res = 0, 0, 0 # Valores por defecto
    if request.method == "POST":
        n1 = float(request.form.get('n1'))
        n2 = float(request.form.get('n2'))
        res = n1 + n2
    return render_template('operasBas.html', n1 = n1, n2 = n2, res = res)

@app.route('/resultado', methods=["GET", "POST"])
def resultado():
    n1 = request.form.get('n1')
    n2 = request.form.get('n2')
    return 'La suma es {}'.format(float(n1) + float(n2))

@app.route("/alumnos", methods=["GET", "POST"])
def alumnos():
    return render_template("alumnos.html")

@app.route('/distancia', methods=["GET", "POST"])
def distancia():
    n1, n2, n3, n4, res = 0, 0, 0, 0, 0
    if request.method == "POST":
        n1 = int(request.form.get('x1'))
        n2 = int(request.form.get('x2'))
        n3 = int(request.form.get('y1'))
        n4 = int(request.form.get('y2'))

        res = ((n2 - n1)**2 + (n3 - n4)**2) ** 0.5
    return render_template('distancia.html', res = res)


@app.route('/usuarios', methods=["GET", "POST"])
def usuarios():
    mat = 0
    nom = ''
    apa = ''
    ama = ''
    email = ''
    usuario_class = forms.UserForm(request.form)
    if request.method == 'POST' and usuario_class.validate():
        mat = usuario_class.matricula.data
        nom = usuario_class.nombre.data
        apa = usuario_class.apaterno.data
        ama = usuario_class.amaterno.data
        email = usuario_class.correo.data
        
        mensaje = 'bienvenido {}'.format(nom)
        flash(mensaje)
    return render_template("usuario.html",form = usuario_class
                           , mat = mat, nom = nom, apa = apa, ama = ama, email = email
                           )
    
if __name__ == '__main__':
    csrf.init_app(app)
    app.run(debug=True)