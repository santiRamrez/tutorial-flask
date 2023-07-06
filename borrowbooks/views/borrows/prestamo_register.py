import functools
import click
import re

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

#For create and check hashed passwords
from werkzeug.security import check_password_hash, generate_password_hash

#Access to the program
from ...controller.dto_escuela_categ import dto_escuela_categ
from ...controller.dto_persona import dto_persona
from ...controller.dto_sede import dto_sede
from ...controller.dto_libro import dto_libro
from ..auth.auth import login_required

#Variable to register this view into the app factory at the borrowbooks/__init__.py file
bp = Blueprint('register_borrows', __name__, url_prefix='/borrow')

@bp.route('/register', methods=('GET', 'POST'))
@login_required
def register():
    data = {}
    
    # Muestra solo los estudiantes y trabajadores (beneficiarios)
    beneficiarios = dto_persona().listar_beneficiarios()
    if beneficiarios:
        data['beneficiarios'] = beneficiarios

    #Muestra todas la sedes de INACAP
    lista_sedes = dto_sede().listar_sedes()
    if lista_sedes:
        data['lista_sedes'] = lista_sedes

    #Muestra todos los ejemplares asociados de esa sede
    lista_libros = dto_libro().listar_libros()
    if lista_libros:
        data['lista_libros'] = lista_libros
   

    #Envía parámetros al servidor para confirmar stock.
    if request.method == 'POST':
        # id_benef = int(request.form['benef'])
        id_sede = int(request.form['sede'])
        isbn = request.form['libro']



        #Send data to create a custom query to check if there is stock.
        #It should return records in this order --> serial number - isbn - titulo - sede - estado
        ejemplares_dispo_x_sede = dto_libro().listar_ejempl_disponib_porsede(isbn, id_sede)
        if ejemplares_dispo_x_sede:
            data['results'] = ejemplares_dispo_x_sede
        
        else:
            flash("No hay copias de ese libro en la sede seleccionada")
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