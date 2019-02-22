from flask import render_template, request, redirect, url_for, abort, flash
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy.sql import text
import bcrypt

from application import app, db
from application.auth.models import User
from application.auth.forms import UsernameAndPasswordForm,UpdatePasswordForm, PasswordForm
from application.discussions import views
from application.tags.forms import SearchTagForm

# Admins only, list all users.
@app.route("/user/users", methods=["GET"])
@login_required
def list_users():
    # If not admin, redirect
    check_user_admin=User.query.get(current_user.id)
    if check_user_admin.role != 'admin':
        return redirect(url_for('discussions_index'))
    stmt=text("SELECT username, id from account")
    users=db.engine.execute(stmt)

    return render_template("user/listusers.html", users=users)
    

# User's profile page
@app.route("/user/<user_id>", methods=["GET"])
@login_required
def user_page(user_id):
    # User cannot access another user's page, but admin can
    check_user_admin=User.query.get(current_user.id)
    try:
        if int(current_user.id) != int(user_id) and check_user_admin.role != 'admin':
            return abort(404)
    except:
        return abort(404)
    stmt = text("select Account.username, Account.id, Account.date_created, Account.role, "
    "count(Message.id) as total_messages from Account LEFT JOIN Message ON Message.account_id = Account.id WHERE Account.id = :id GROUP BY Account.username, Account.id").params(id = user_id)

    user=db.engine.execute(stmt).fetchone()
    return render_template("user/userpage.html", user = user)



# Update user's password
@app.route("/user/<user_id>/change", methods=["POST"])
@login_required
def update_password(user_id):
    try:
        if int(current_user.id) != int(user_id):
            return abort(404)
    except:
        return abort(404)

    form = UpdatePasswordForm(request.form)
    if not form.validate():
        return render_template("user/userpage.html", error = "Problem validating passwords. Make sure the new password is atleast 8 characters, and that given new passwords match.", 
        user=current_user, form = UpdatePasswordForm())

    #Find user from database to compare passwords
    stmt=text("SELECT*FROM Account WHERE Account.id = :id").params(id=current_user.id)

    user = db.engine.execute(stmt).fetchone()

    # Compare given old password to password in database
    if not bcrypt.checkpw(form.old_password.data.encode('utf8'), user._password.encode('utf8')):
        return render_template("user/userpage.html", form = form,
                           error = "Wrong old password", user=current_user)

    # Hash new password and update user's password in database
    pwd = bcrypt.hashpw(form.new_password.data.encode('utf8'), bcrypt.gensalt()).decode('utf8')
    stmt=text("UPDATE Account SET _password = :new, date_modified = current_timestamp WHERE Account.id = :id").params(new=pwd, id=current_user.id)
    user=db.engine.execute(stmt)

    return render_template("user/changepasswordform.html", success = "Password updated.", user=current_user, form = UpdatePasswordForm())



# Get page for user-delete form.
@app.route("/user/<user_id>/delete", methods=["GET"])
@login_required
def get_delete_user(user_id):
    try:
        if int(current_user.id) != int(user_id):
            return abort(404)
    except:
        return abort(404)
    
    return render_template("user/deleteuser.html", form = PasswordForm())

#Delete user
@app.route("/user/<user_id>/delete", methods=["POST"])
@login_required
def delete_user(user_id):
    check_user_admin=User.query.get(current_user.id)
    # Admin can delete any user
    try:
        if int(current_user.id) != int(user_id) and check_user_admin.role != 'admin':
            return abort(404)
    except:
        return abort(404)
    
    form=PasswordForm(request.form)

    # Confirm password before delete, if the one doing the delete is not admin
    if check_user_admin.role != 'admin':
        stmt=text("SELECT*FROM Account WHERE Account.id = :id").params(id=user_id)
        user = db.engine.execute(stmt).fetchone()
        if not bcrypt.checkpw(form.password.data.encode('utf8'), user._password.encode('utf8')):
            return render_template("user/deleteuser.html", form = PasswordForm(), error = "Wrong password.")
    
    # Delete related messages
    stmt=text("DELETE FROM Message WHERE Message.account_id = :id").params(id=user_id)
    db.engine.execute(stmt)

    # Delete related discussions
    stmt=text("DELETE FROM Discussion WHERE Discussion.account_id = :id").params(id=user_id)
    db.engine.execute(stmt)

    # Delete account
    stmt=text("DELETE FROM Account WHERE Account.id = :id").params(id=user_id)
    db.engine.execute(stmt)

    if check_user_admin.role == 'admin':
        return redirect(url_for("list_users"))
    logout_user()

    return render_template("auth/loginform.html", success = "Account successfully deleted.", form = UsernameAndPasswordForm())


# Get page for changing user's password
@app.route("/user/<user_id>/change", methods=["GET"])
@login_required
def get_change_password_form(user_id):
    return render_template("user/changepasswordform.html", form = UpdatePasswordForm(), user = current_user)