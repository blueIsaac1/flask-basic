from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def mainPage():
    return render_template("main.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/clientes")
def clientes():
    clientes = ["Cliente João da Silva", "Cliente Maria da Silva", "Cliente Joana da Silva",
                "Cliente Pedro da Silva", "Cliente José da Silva"]
    return render_template('clientes.html', clientes=clientes)

@app.route("/funcionarios")
def funcionarios():
    funcionarios = ["Funcionario João da Silva", "Funcionario Maria da Silva", "Funcionario Joana da Silva",
                "Funcionario Pedro da Silva", "Funcionario José da Silva"]
    return render_template('funcionarios.html', funcionarios=funcionarios)
