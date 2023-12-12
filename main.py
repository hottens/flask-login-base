from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)

title = 'Power Progress'

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.context_processor
def utility_processor():
    def get_title():
        return "Power Progress"
    return dict(get_title=get_title)