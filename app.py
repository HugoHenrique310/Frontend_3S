from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'shhh'

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/calculos')
def calculos():
    return render_template("calculos.html")

@app.route('/funcionarios')
def funcionarios():
    return render_template("funcionarios.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@app.route('/operacoes')
def operacoes():
    return render_template("operacoes.html")


@app.route('/somar', methods=['GET', 'POST'])
def somar():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            soma = n1 + n2
            flash("Soma realizada", "alert-success")
            return render_template("operacoes.html", n1=n1, n2=n2, soma=soma)
        else:
            #passo 1: emitir a mensagem e a categoria do flash
            flash("Preencha o campo para realizar a soma", 'alert-danger')

    return render_template("operacoes.html")


@app.route('/subtrair', methods=['GET', 'POST'])
def subtrair():
    if request.method == 'POST':
        if request.form['form-n1'] and request.form['form-n2']:
            n1 = int(request.form['form-n1'])
            n2 = int(request.form['form-n2'])
            subtrair = n1 - n2
            flash("Subtração realizada", "alert-success")
            return render_template("operacoes.html", n1=n1, n2=n2, subtrair=subtrair)
        else:
            flash("Preencha o campo para realizar a subtração", 'alert-danger')
        return render_template("operacoes.html")


@app.route('/multiplicar', methods=['GET', 'POST'])
def multiplicar():
    if request.method == 'POST':
        if request.form['form*n1'] and request.form['form*n2']:
            n1 = int(request.form['form*n1'])
            n2 = int(request.form['form*n2'])
            multiplicar = n1 * n2
            flash("Multiplicação realizada", "alert-success")
            return render_template("operacoes.html", n1=n1, n2=n2, multiplicar=multiplicar)
        else:
            flash("Preencha o campo para realizar a multiplicação", 'alert-danger')
        return render_template("operacoes.html")


@app.route('/dividir', methods=['GET', 'POST'])
def dividir():
    if request.method == 'POST':
        if request.form['form/n1'] and request.form['form/n2']:
            n1 = int(request.form['form/n1'])
            n2 = int(request.form['form/n2'])
            dividir = n1 / n2
            flash("Divisão realizada", "alert-success")
            return render_template("operacoes.html", n1=n1, n2=n2, dividir=dividir)
        else:
            flash("Preencha o campo para realizar a soma", 'alert-danger')
        return render_template("operacoes.html")


@app.route('/geometria')
def geometria():
    return render_template("geometria.html")

@app.route('/triangulo', methods=['GET', 'POST'])
def triangulo():
    if request.method == 'POST':
        if request.form['form-n1']:
            n1 = int(request.form['form-n1'])
            perimetro = n1 + n1 + n1
            area = n1 / n1 /2
            flash("Conta realizada com sucesso", "alert-success")
            return render_template("geometria.html", n1=n1, perimetro=perimetro, area=area)
        else:
            flash("Preencha o campo para realizar a conta", 'alert-danger')
        return render_template("geometria.html")

@app.route('/circulo', methods=['GET', 'POST'])
def circulo():
    if request.method == 'POST':
        n2 = int(request.form["form-n2"])
        perimetro_2 = 2 * 3.14 * n2
        area_2 = 3.14 * n2 ** 2
        flash("Conta realizada com sucesso", "alert-success")
        return render_template("geometria.html", n2=n2, perimetro_2=perimetro_2, area_2=area_2)
    else:
        flash("Preencha o campo para realizar a conta", 'alert-danger')
    return render_template("geometria.html")

@app.route('/quadrado', methods=['GET', 'POST'])
def quadrado():
    if request.method == 'POST':
        n3 = int(request.form["form-n3"])
        perimetro_3 = n3 * 4
        area_3 = n3 * n3
        flash("Conta realizada com sucesso", "alert-success")
        return render_template("geometria.html", n3=n3, perimetro_3=perimetro_3, area_3=area_3)
    else:
        flash("Preencha o campo para realizar a conta", 'alert-danger')
    return render_template("geometria.html")

@app.route('/hexagono', methods=['GET', 'POST'])
def hexagono():
    if request.method == 'POST':
        n4 = int(request.form['form-n4'])
        perimetro_4 = n4 * 6
        area_4 = n4 * n4 / 2 * 6
        flash("Conta realizada com sucesso", "alert-success")
        return render_template("geometria.html", n4=n4, perimetro_4=perimetro_4, area_4=area_4)
    else:
        flash("Preencha o campo para realizar a conta", 'alert-danger')
    return render_template("geometria.html")



if __name__ == '__main__':
    app.run(debug=True)