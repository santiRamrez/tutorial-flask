import functools
import click

from flask import (
    Blueprint, flash, redirect, render_template, request, session, url_for
)

#For create and check hashed passwords
from werkzeug.security import check_password_hash, generate_password_hash

#Access to the program
from ..controller.dto_persona import dto_persona


#Variable to register this view into the app factory at the borrowbooks/__init__.py file
bp = Blueprint('auth', __name__, url_prefix='/auth')
#------------------------------------------------------------

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        #Recibe datos del usuario.
        run = request.form['run'].upper()
        password = request.form['password']
        hashed_pw = generate_password_hash(password)

        #Transfiere y recibe datos del controlador
        user = dto_persona().login_persona(run, password)
        if user:
            session.clear()
            session['user_id'] = user.run
            session['nombre'] = user.nombre
            #Go to the file home and then access to the home function
            return redirect(url_for('gerente.menu'))

        else:
            mensaje = "La contraseña o el run no es correcto"
            return render_template('auth/login.html', msg=mensaje)
        
    return render_template('auth/login.html')

#-----------------------------------------------------------

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        session.clear()

#----------------------------------------------------------

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session.get('user_id') is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view