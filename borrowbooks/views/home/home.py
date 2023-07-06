# import functools
# import click

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

#Access to the program
from ...controller.dto_libro import dto_libro

#Variable to register this view into the app factory at the borrowbooks/__init__.py file
bp = Blueprint('home', __name__)
@bp.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
      #Libros data structure should be [{}, {}, {}]
      libros = dto_libro().listar_libros() if dto_libro().listar_libros() else "No hay libros"
      return render_template('home/index.html', libros=libros)
