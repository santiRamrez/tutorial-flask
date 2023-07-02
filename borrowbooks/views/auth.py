import functools
import click

from flask import (
    Blueprint, flash, redirect, render_template, request, session, url_for
)

#For create and check hashed passwords
from werkzeug.security import check_password_hash, generate_password_hash

#Access to the program
from ..controller.dto_persona import dto_persona
from ..controller.dto_perfil import dto_perfil
from ..controller.dto_sede import dto_sede


#Variable to register this view into the app factory at the borrowbooks/__init__.py file
bp = Blueprint('auth', __name__, url_prefix='/auth')
#------------------------------------------------------------

@bp.route('/login', methods=('GET', 'POST'))
def login():
    usuario_perfil = {}
    usuario_sede = {}

    #Carga datos de perfiles, sedes y de personas en memoria local
    listado_personas = dto_persona().carga_personas_memoria()
    listado_sedes = dto_sede().listar_sedes()
    listado_perfiles = dto_perfil().listar_perfiles_usuarios(True)

    if listado_perfiles and listado_personas:
        for per in listado_personas:
            per_id = per.perfil_id
            for cargo in listado_perfiles:
                if per_id == cargo.id:
                    usuario_perfil[per.run] = cargo.descrip
                    break
                    
    if listado_sedes and listado_personas:
        for per in listado_personas:
            per_id = per.sede_id
            for sede in listado_sedes:
                if per_id == sede.id:
                    usuario_sede[per.run] = sede.descrip
                    break
        

    if request.method == 'POST':
        #Recibe datos del usuario.
        run = request.form['run'].upper()
        password = request.form['password']

        #Pasa datos al controlador para validar credenciales
        user_logged = dto_persona().login_persona(run, password)
        if user_logged:
            session.clear()
            session['user_id'] = user_logged.run
            selected_view = usuario_perfil[user_logged.run]
            #Change the id to the description
            user_logged.perfil_id = selected_view.lower()
            user_logged.sede_id = usuario_sede[user_logged.run]
            #Add the string of the user logged to the session object
            session['user_str'] = user_logged.__str__()

            #Go to the view file and then access to the main function
            return redirect(url_for(f'{selected_view.lower()}.menu'))

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

#-------------------------------------------------------
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home.home'))