from flask import Flask, render_template, url_for, flash, request, redirect

from api_routes import routes
from database import db_session, Funcionario
from sqlalchemy import select, and_, func
from flask_login import LoginManager, login_required, login_user, logout_user, current_user

app = Flask(__name__)
# mover para .env
app.config['SECRET_KEY'] = '1234'

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@login_manager.user_loader
def load_user(user_id):
    user = select(Funcionario).where(Funcionario.id == int(user_id))
    resultado = db_session.execute(user).scalar_one_or_none()
    return resultado


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/calculos')
def calculos():
    return render_template("calculos.html")


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
            # passo 1: emitir a mensagem e a categoria do flash
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
            area = n1 / n1 / 2
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


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('form-email')
        senha = request.form.get('form-senha')

        if email and senha:
            verificar_email = select(Funcionario).where(Funcionario.email == email)
            resultado_email = db_session.execute(verificar_email).scalar_one_or_none()
            if resultado_email:
                if resultado_email.check_password(senha):
                    login_user(resultado_email)
                    flash(f'Logado com sucesso!', 'success')
                    return redirect(url_for('home'))
                else:
                    flash(f'Senha incorreta!', 'danger')
                    return redirect(url_for('login'))
            else:
                flash('email não encontrado!')
                return redirect(url_for('login'))
        else:
            flash('Preencha os campos!', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    logout_user()
    flash('Logout com sucesso', 'success')
    return redirect(url_for('home'))


@app.route('/funcionarios', methods=['GET', 'POST'])
@login_required
def funcionarios():
    funcionarios_sql = select(Funcionario)
    funcionarios_resultado = db_session.execute(funcionarios_sql).scalars().all()

    return render_template('funcionarios.html', lista_funcionarios=funcionarios_resultado)


@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        # 1. Pegar dados (Cuidado com o nome form-salario)
        nome = request.form.get('form-nome')
        email = request.form.get('form-email')
        senha = request.form.get('form-senha')
        salario_raw = request.form.get('form-salario')

        # 2. Validar salário para não travar o float
        salario_val = float(salario_raw) if salario_raw and salario_raw.strip() else 0.0

        # 3. Verificar se o e-mail já existe
        ver_email = select(Funcionario).where(Funcionario.email == email)
        exists_email = db_session.execute(ver_email).scalar_one_or_none()

        if exists_email:
            flash(f'Email {email} já cadastrado', 'danger')
            return redirect(url_for('funcionarios'))

        try:
            novo_funcionario = Funcionario(
                nome=nome,
                email=email,
                data_nascimento=request.form.get('form-nascimento'),
                cpf=request.form.get('form-cpf'),
                cargo=request.form.get('form-cargo'),
                salario=salario_val
            )
            novo_funcionario.set_password(senha)
            db_session.add(novo_funcionario)
            db_session.commit()
            flash(f'Funcionario {nome} cadastrado!', 'success')
        except Exception as e:
            db_session.rollback()
            print(f"ERRO DE DEBUG: {e}")  # Olhe o terminal aqui!
            flash(f'Erro: {e}', 'danger')

    return redirect(url_for('funcionarios'))


@app.route('/animais')
def animais():
    return render_template("animais.html")

@app.route('/gatos')
def listar_gatos():
    gatos = routes.get_gatos()

    for gato in gatos:
        gato["temperament"] = gato["temperament"].split(',')
        gato["image"] = routes.get_image()["url"]

    return render_template('gatos.html', gatos=gatos)


if __name__ == '__main__':
    app.run(debug=True, port=5000)