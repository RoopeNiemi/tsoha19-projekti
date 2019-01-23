from flask import render_template, request, redirect, url_for, abort, flash
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy.sql import text

from application import app, db, bcrypt
from application.auth.models import User
from application.auth.forms import UsernameAndPasswordForm,UpdatePasswordForm, PasswordForm
from application.discussions import views

@app.route("/user/<user_id>", methods=["GET"])
@login_required
def user_page(user_id):
    # User cannot access another user's page
    try:
        if int(current_user.id) != int(user_id):
            return abort(404)
    except:
        return abort(404)
    stmt = text("select Account.username, Account.id, Account.date_created, "
    "count(Message.id) as total_messages from Message, Account where Message.account_id = Account.id AND Account.id = :id").params(id = current_user.id)

    db.engine.execute(stmt).fetchone()
    return render_template("user/userpage.html", user = current_user)


@app.route("/user/<user_id>/change", methods=["POST"])
@login_required
def update_password(user_id):
    try:
        if int(current_user.id) != int(user_id):
            return abort(404)
    except:
        return abort(404)

    form = UpdatePasswordForm(request.form)
    if not form.validate_form():
        #TODO: use validators for better error messaging and validation
        render_template("user/userpage.html", error = "Problem validating passwords", user=current_user, form = UpdatePasswordForm())

    #Find user from database to compare passwords
    stmt=text("SELECT*FROM Account WHERE Account.id = :id").params(id=current_user.id)

    user = db.engine.execute(stmt).fetchone()

    # Compare given old password to password in database
    if not bcrypt.check_password_hash(user._password, form.old_password.data):
        return render_template("auth/userpage.html", form = form,
                           error = "Wrong old password", user=current_user)

    # Hash new password and update user's password in database
    pwd = bcrypt.generate_password_hash(form.new_password.data)
    stmt=text("UPDATE Account SET _password = :new, date_modified = current_timestamp WHERE Account.id = :id").params(new=pwd, id=current_user.id)
    user=db.engine.execute(stmt)

    return render_template("user/userpage.html", error = "Password updated", user=user, form = UpdatePasswordForm())




@app.route("/user/<user_id>/delete", methods=["GET"])
@login_required
def get_delete_user(user_id):
    try:
        if int(current_user.id) != int(user_id):
            return abort(404)
    except:
        return abort(404)
    
    return render_template("user/deleteuser.html", form = PasswordForm())

@app.route("/user/<user_id>/delete", methods=["POST"])
@login_required
def delete_user(user_id):
    try:
        if int(current_user.id) != int(user_id):
            return abort(404)
    except:
        return abort(404)
    
    form=PasswordForm(request.form)

    # Confirm password before delete
    stmt=text("SELECT*FROM Account WHERE Account.id = :id").params(id=current_user.id)
    user = db.engine.execute(stmt).fetchone()
    if not bcrypt.check_password_hash(user._password, form.password.data):
        return render_template("user/deleteuser.html", form = PasswordForm(), error = "Wrong password.")
    
    # Delete related discussions
    stmt=text("DELETE FROM Discussion WHERE Discussion.account_id = :id").params(id=current_user.id)
    db.engine.execute(stmt)

    # Delete related messages
    stmt=text("DELETE FROM Message WHERE Message.account_id = :id").params(id=current_user.id)
    db.engine.execute(stmt)

    # Delete account
    stmt=text("DELETE FROM Account WHERE Account.id = :id").params(id=current_user.id)
    db.engine.execute(stmt)


    logout_user()

    return render_template("auth/loginform.html", error = "Account successfully deleted.", form = UsernameAndPasswordForm())

@app.route("/user/<user_id>/change", methods=["GET"])
@login_required
def get_change_password_form(user_id):
    return render_template("user/changepasswordform.html", form = UpdatePasswordForm(), user = current_user)