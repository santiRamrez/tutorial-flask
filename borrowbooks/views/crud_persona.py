import functools
import click

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

#For create and check hashed passwords
from werkzeug.security import check_password_hash, generate_password_hash

#Access to the program
from ..controller.dto_persona import dto_persona
from .auth import login_required

#Variable to register this view into the app factory at the borrowbooks/__init__.py file
bp = Blueprint('register_user', __name__, url_prefix='/user')


@bp.route('/register', methods=('GET', 'POST'))
@login_required
def register():
    if request.method == 'POST':
        #Recibe datos del usuario.
        nombre = request.form['nombre'].upper()
        apellido_pat = request.form['apellido_pat'].upper()
        apellido_mat = request.form['apellido_mat'].upper()
        run = request.form['run'].upper()
        fono = request.form['fono']
        fecha_nacim = '1998-09-11'
        email = request.form['email'].upper()
        password = request.form['password'].upper()
        hashed_pw = generate_password_hash(password)

        error = None

        if error is None:
          #Transfiere datos hacia el controlador
          action = dto_persona().agregar_persona(nombre, apellido_pat, apellido_mat, run, fono, fecha_nacim, email, 1, 1, password)
          if action:
             flash("Estamos Ok")

    return render_template('auth/register.html')

#------------------------------------------------------------