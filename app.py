import ttg
from flask import Flask, render_template, request, flash,redirect, url_for
from werkzeug.exceptions import HTTPException


# agregue: session
import functools
import os # Para generar el aleatorio

app = Flask(__name__)

app.secret_key = os.urandom( 24 ) # reemplace por esta.


@app.route( '/' ) # función de entrada
def index():
  return render_template("index.html")

@app.route( '/calcular' ,methods=('GET', 'POST')) # función de entrada
def calcular():
    if request.method == 'POST':
        
        list_exp = []
        args = request.form['args']
        exp = request.form['exp']
        table = ttg.Truths(args.split(","),exp.split(","))
        
    return render_template("index.html",table = table,args=args,exp = exp)

@app.route( '/valuation' ,methods=('GET', 'POST')) # función de entrada
def valuation():
    if request.method == 'POST':
      
        num = int(request.form['col'])
        args = request.form['args']
        exp = request.form['exp']
        table = ttg.Truths(args.split(","),exp.split(","))
        
    return render_template("index.html", val = table.valuation(num),table = table,args=args,exp = exp)

@app.errorhandler(Exception)
def handle_exception(e):
    flash(str(e))
    return redirect( url_for( 'index' ) )

