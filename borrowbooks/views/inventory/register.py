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
from ...controller.dto_sede import dto_sede
from ...model.sede import sede as Sede
from ..auth.auth import login_required

#Variable to register this view into the app factory at the borrowbooks/__init__.py file
bp = Blueprint('register_book', __name__, url_prefix='/inventory')


@bp.route('/register', methods=('GET', 'POST'))
@login_required
def register():
    #Carga información necesaria para la vista
    data = {}

    libros = dto_libro().listar_libros()
    if libros:
        data['libros'] = libros
    
    categorias = dto_escuela_categ().listar_categorias()
    if categorias:
        data['categorias'] = categorias

    sedes = dto_sede().listar_sedes()
    if sedes:
        data['sedes'] = sedes

    txt = session.get('user_str')
    data['sede'] = txt[txt.index("INACAP"):].strip()
       
    
    if request.method == 'POST':
        #Si está activo el modal stock y recibe datos de esa etiqueta form para ASIGNAR STOCK POR SEDE
        if request.form['stock'] == 'on':
            #Inicia proceso de agregar stock por libro.
            sede_stock = int(request.form['stockSede'])
            libro_stock = request.form['stockLibro']
            qty_stock = int(request.form['qtyStock'])

            inicia_sede = Sede()
            txt_selected_sede = inicia_sede.filtra_por_id(sede_stock)
        
            num_agregados = dto_libro().agregar_qty_ejemplares(libro_stock, sede_stock, qty_stock)
            if num_agregados > 0:
                flash(f"Se han agregado {num_agregados} unidades a la sede {txt_selected_sede.descrip}")
            
    
        else:
        #Crea registro de un libro nuevo
            isbn = request.form['isbn']
            titulo = request.form['titulo']
            editorial = request.form['editorial']
            autores = request.form['autores'].upper()
            year = request.form['year']
            idioma = request.form['idioma']
            categoria = int(request.form['categoria'])
            sede = request.form['sede']

            #Transfiere datos hacia el controlador
            action1 = dto_libro().agregar_libro(isbn, titulo, editorial, year, 0, autores, idioma, categoria, 1)
            if action1:
                action2 = dto_libro().agregar_ejemplar(isbn, sede, 0, 0, 1)
                if action2:
                    flash(f"Se ha agregado 1 unidad a {sede}")
                    # return redirect(url_for('home.home'))
            
            else:
                flash("Hay un error")

        

    return render_template('dashboard/book.html', data=data)