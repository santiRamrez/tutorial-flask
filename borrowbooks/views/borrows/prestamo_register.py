import functools
import click
import re

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

#For create and check hashed passwords
from werkzeug.security import check_password_hash, generate_password_hash

#Access to the program
from ...controller.dto_libro import dto_libro
from ...controller.dto_escuela_categ import dto_escuela_categ
from ..auth.auth import login_required

#Variable to register this view into the app factory at the borrowbooks/__init__.py file
bp = Blueprint('register_borrow', __name__, url_prefix='/borrow')

@bp.route('/register', methods=('GET', 'POST'))
@login_required
def register():
    data = {}
    
    
       


    # if request.method == 'POST':
    #     #Recibe datos del usuario.
    #     isbn = request.form['isbn']
    #     titulo = request.form['titulo']
    #     editorial = request.form['editorial']
    #     autores = request.form['autores'].upper()
    #     year = request.form['year']
    #     idioma = request.form['idioma']
    #     categoria = int(request.form['categoria'])
    #     sede = request.form['sede']
    #     nserie = titulo[0:2].upper() + request.form['serialnum']

    #     #Transfiere datos hacia el controlador
    #     action1 = dto_libro().agregar_libro(isbn, titulo, editorial, year, 0, autores, idioma, categoria, 1)
    #     if action1:
    #         action2 = dto_libro().agregar_ejemplar(nserie, isbn, sede, 0, 0, 1)
    #         if action2:
    #             flash("Operacion OK")
    #             # return redirect(url_for('home.home'))
        
    #     else:
    #         flash("Hay un error")

    return render_template('dashboard/borrow/register.html', data=data)