import os
from flask import Flask

# This function is the app factory

def create_app(test_config=None):
    
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #Blueprint for render home view
    from .views import home
    app.register_blueprint(home.bp)

    #Blueprint for authentication view
    from .views import auth
    app.register_blueprint(auth.bp)

    #Blueprint for register and modify user's data view
    from .views import crud_persona
    app.register_blueprint(crud_persona.bp)

    #Blueprint for register and modify book's data view
    from .views import crud_libro
    app.register_blueprint(crud_libro.bp)

    #Blueprint for register and modify borrow's data view
    from .views import crud_prestamo
    app.register_blueprint(crud_prestamo.bp)

    #Make a blueprint for GERENTE view
    from .views import gerente
    app.register_blueprint(gerente.bp)

    #Make a blueprint for ENCARGADO view
    from .views import encargado
    app.register_blueprint(encargado.bp)

    #Make a blueprint for ASISTENTE view
    from .views import asistente
    app.register_blueprint(asistente.bp)

    return app
