# This is the main starting point of the Flask application
from flask import Flask, request

from config import Config
import os

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from app.routes import bp as bp_routes
    app.register_blueprint(bp_routes, url_prefix='/api')

    @app.route('/')
    def root_endpoint():
        return 'Flask Application Named: \"' + os.environ['FLASK_APP'] + '\" Running!!'
  
    @app.route('/search')
    def search():
        query = request.args.get('type', default='')
        return f'Search Results for: {query}'

    return app
