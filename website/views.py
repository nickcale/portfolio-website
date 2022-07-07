from flask import Blueprint, render_template


views = Blueprint('views', __name__)


@views.route('/')
def get_home():
    return render_template('home.html')


@views.route('/about')
def get_about():
    return render_template('about.html')


@views.route('/projects')
def get_projects():
    return render_template('projects.html')