# load secret key environment variable 
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
# import flask
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('APP_CONFIG_KEY')

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app
