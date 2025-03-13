from flask import Blueprint, render_template
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('index.html')
