from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from ..models import User
from werkzeug.security import generate_password_hash, check_password_hash

from ..extensions import db

from flask_login import login_user, login_required, logout_user, current_user

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            flash('Logged in successfully!', category='success')
            login_user(user, remember=True)
            return redirect(url_for('home.home'))
        else:
            flash('Incorrect data, try again.', category='error')

    return render_template("login.html", user=current_user)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.home'))


@auth_bp.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(username=username).first()
        if user:
            flash('Nuh-uh, this username is taken.', category='error')
        else:
            creation_flag = True
            if len(username) < 4:
                flash('Nickname must be greater than 3 characters.',
                      category='error')
                creation_flag = False
            if password1 != password2:
                flash('Passwords do not match.', category='error')
                creation_flag = False
            if len(password1) < 6:
                flash('Password must be at least 6 characters.', category='error')
                creation_flag = False

            if creation_flag:
                if ('language' in session):
                    new_user = User(username=username, password=generate_password_hash(
                        password1, method='scrypt'), preferred_locale=session['language'] )
                else:
                    new_user = User(username=username, password=generate_password_hash(
                        password1, method='scrypt'))
                db.session.add(new_user)
                db.session.commit()

                flash('Account created!', category='success')

                return redirect(url_for('auth.login'))

    return render_template("sign_up.html", user=current_user)
