import functools
import click

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

#For create and check hashed passwords
from werkzeug.security import check_password_hash, generate_password_hash

#Access to the program
from ..controller.dto_persona import dto_persona
from ..controller.dto_perfil import dto_perfil
from ..controller.dto_sede import dto_sede
from .auth import login_required

#Variable to register this view into the app factory at the borrowbooks/__init__.py file
bp = Blueprint('register_user', __name__, url_prefix='/user')


@bp.route('/register', methods=('GET', 'POST'))
@login_required
def register():
    data = {}
    if request.method == 'GET':
        #Add data to render profiles
        perfiles = dto_perfil().listar_perfiles_usuarios()
        if perfiles:
            data['perfiles'] = perfiles
        
        else:
            data['perfiles'] = 'No hay perfiles, intente presionando F5 para recargar'
        
        #Add data to render locations
        sedes = dto_sede().listar_sedes()
        if sedes:
            data['sedes'] = sedes
        else:
            data['sedes'] = 'No hay sedes, intente presionando F5 para recargar'


    if request.method == 'POST':
        #Recibe datos del usuario.
        nombre = request.form['nombre']
        apellido_pat = request.form['apellido_pat']
        apellido_mat = request.form['apellido_mat']
        run = request.form['run'].upper()
        fono = request.form['fono']
        fecha_nacim = request.form['day_birth']
        email = request.form['email']
        password = request.form['password']
        # hashed_pw = generate_password_hash(password)
        cargo = request.form['cargo']
        sede = request.form['sede']

        #Transfiere datos hacia el controlador
        action = dto_persona().agregar_persona(nombre, apellido_pat, apellido_mat, run, fono, fecha_nacim, email, cargo, sede, password)
        if action:
            flash("Estamos Ok")

    return render_template('auth/register.html', data=data)

#------------------------------------------------------------

