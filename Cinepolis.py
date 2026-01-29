from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/CINECO', methods=["GET", "POST"])
def operas1():
    numeroBoletos, costoBoletos = 0, 12
    metodoPago, nombre = "", ""
    if request.method == "POST":
        numeroBoletos = int(request.form.get('boletos'))
        metodoPago = request.form.get('metodoPago')
        nombre = request.form.get('nombre')
        costoBoletos = costoBoletos * numeroBoletos
        if numeroBoletos > 5:
            costoBoletos *= 0.85  # Aplicar 15% de descuento
        elif numeroBoletos >= 3:
            costoBoletos *= 0.90  # Aplicar 10% de descuento
        if metodoPago == "CINECO":
            costoBoletos *= .90  # Aplicar 10% de descuento

    return render_template('cinepolis.html', numeroBoletos = numeroBoletos, costoBoletos = costoBoletos, nombre = nombre)
if __name__ == '__main__':
    app.run(debug=True)