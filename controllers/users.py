from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required

users_bp = Blueprint(name='users', 
    import_name=__name__,
    url_prefix='/users')

@users_bp.route('/')
@login_required
def index():
    return render_template('users/index.html')


