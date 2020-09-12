# Module app.
# Description: Create Flask app, import blueprint
# combine Flask and SOAP services.
# Author : Dung Ho
# Email: dung.ho@edu.turkuamk.fi


from controllers.api import api
from controllers.soap import wsgi_application as soap
from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware


def create_app():
    # Create a Flask application
    app = Flask(
        __name__,
        template_folder='templates',
        static_folder='static',
    )

    # Register Blueprint
    app.register_blueprint(api)

    # Using DispatcherMiddleware to combine Flask and SOAP services
    app.wsgi_app = DispatcherMiddleware(
        app.wsgi_app,
        {
            '/soap': soap
        }
    )

    return app
