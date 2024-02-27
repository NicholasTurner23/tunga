from app.users import userbp
from flask_login import login_user, login_required, logout_user
from flask import flash, redirect, render_template, url_for
from .models import User
from app import get_loginmanager, utils
from .forms import RegistrationFrom, LoginForm
from app import get_db

db = get_db()

loginmanager = get_loginmanager()

@loginmanager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@userbp.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationFrom()
    if form.validate_on_submit():
        hashed_password = utils.hash(form.password.data)
        user = User(
            username = form.username.data,
            email = form.email.data,
            password = hashed_password
        )
        db.session.add(user)
        db.session.commit()
        flash('Successfully signed up!.', 'success')
        return redirect("/login")
    return render_template("register.html", form=form)


@userbp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        password = form.password.data
        user = User.query.filter_by(email=form.email.data).first()
        if user and utils.verify(password, user.password):
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect('/posts')
    else:
        flash('Invalid username or password', 'error')
    return render_template("login.html", form=form)

@userbp.route("/logout")
@login_required
def logout():
    logout_user()
    flash('logged out successfully!', 'success')
    return redirect(url_for('login'))
