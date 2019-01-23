from flask import render_template, request, redirect, url_for, abort, flash
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy.sql import text

from application import app, db, bcrypt
from application.auth.models import User
from application.auth.forms import UsernameAndPasswordForm,UpdatePasswordForm, PasswordForm, CreateUserNamePasswordForm
from application.discussions import views

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = UsernameAndPasswordForm())

    form = UsernameAndPasswordForm(request.form)

    user = User.query.filter_by(username=form.username.data).first()
    if not user or not user.is_correct_password(form.password.data):
        return render_template("auth/loginform.html", form = form,
                           error = "Wrong username or password")
    else:
        login_user(user)
        return redirect(url_for("discussions_index"))
 

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("auth_login"))    

@app.route("/auth/register", methods=["GET", "POST"])
def auth_register():
    if request.method == "GET":
        return render_template("auth/registerform.html", form = CreateUserNamePasswordForm())
        
    form = CreateUserNamePasswordForm(request.form)
    if not form.validate_form():
        return "no"
    user = User(username=form.username.data, password = bcrypt.generate_password_hash(form.password.data))
    db.session().add(user)
    db.session().commit()
    return render_template("auth/loginform.html", form = UsernameAndPasswordForm())
