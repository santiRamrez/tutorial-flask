import functools
import click
import re

from flask import (
    Blueprint, flash, redirect, render_template, request, session, url_for
)

#For create and check hashed passwords
from werkzeug.security import check_password_hash, generate_password_hash

#Access to the program
# from ...controller.dto_persona import dto_persona
from ..auth.auth import login_required

#Variable to register this view into the app factory at the borrowbooks/__init__.py file
bp = Blueprint('gerente', __name__, url_prefix='/user')

@bp.route('/gerente', methods=('GET', 'POST'))
@login_required
def menu():
    data = {}
    txt = session.get('user_str')
    data['sede'] = txt[txt.index("INACAP"):]
    lista = txt.split(" ")
    filtered = [val for val in lista if len(val) > 0]
    data['nombre'] = filtered[1] + " " + filtered[2]
    data['perfil'] = filtered[5].capitalize()
  
    return render_template('dashboard/gerente.html', data=data)