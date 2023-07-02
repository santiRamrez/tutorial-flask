import click

from flask import (
    Blueprint, flash, redirect, render_template, request, session, url_for
)

#For create and check hashed passwords
from werkzeug.security import check_password_hash, generate_password_hash

#Access to the program
from ..controller.dto_persona import dto_persona
from .auth import login_required

#Variable to register this view into the app factory at the borrowbooks/__init__.py file
bp = Blueprint('asistente', __name__, url_prefix='/user')

@bp.route('/asistente', methods=('GET', 'POST'))
@login_required
def menu():
    data = {}
    txt = session.get('user_str')
    data['sede'] = txt[txt.index("INACAP"):]
    lista = txt.split(" ")
    data['nombre'] = lista[1] + " " + lista[2]
    data['perfil'] = lista[5].capitalize()
  
    return render_template('dashboard/asistente.html', data=data)