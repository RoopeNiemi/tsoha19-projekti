from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.sql import text
from application import app, db
from application.auth.models import User
from application.discussions.models import Discussion
from application.messages.models import Message
from application.discussions.forms import DiscussionForm, CommentForm

@app.route("/")
def index():
    return redirect(url_for("discussions_index"))

@app.route("/discussions", methods=["GET"])
def discussions_index():
    stmt = text("SELECT Account.username as username, Discussion.id as d_id, "
    "Discussion.title as title, Discussion.date_created as d_date_created, "
    "count(Message.id) as totalmessages, max(Message.date_created) as latest_message from Message, Discussion, "
    "Account where Account.id = Discussion.account_id AND Message.discussion_id = Discussion.id "
    "GROUP BY Discussion.title ORDER BY latest_message DESC")
    discussions = db.engine.execute(stmt)
    return render_template("discussions/list.html", discussions=discussions)

@app.route("/discussions/new")
@login_required
def discussions_form():
    return render_template("discussions/new.html", form = DiscussionForm())


@app.route("/discussions", methods=["POST"])
@login_required
def discussions_create():
    form = DiscussionForm(request.form)
    #TODO: validate input somehow
    discussion = Discussion(form.title.data)
    discussion.set_account_id(current_user.id)
    db.session().add(discussion)
    db.session().commit()

    message = Message(form.content.data)
    message.set_account_id(current_user.id)
    message.set_discussion_id(discussion.id)

    db.session().add(message)
    db.session().commit()

    return redirect(url_for("discussions_index"))


@app.route("/discussions/<discussion_id>", methods=["GET"])
def discussions_show(discussion_id):
    stmt = text("SELECT Account.username AS account_username, "
                "Account.date_created AS account_date_created, "
                "Message.content AS message_content, "
                "Message.date_created AS message_date_created "
                "FROM Account, Message, Discussion WHERE Account.id = Message.account_id "
                "AND Discussion.id = Message.discussion_id " 
                "AND Discussion.id = :id").params(id = discussion_id)

    comments = db.engine.execute(stmt)
    stmt = text("SELECT Discussion.id AS id, Discussion.title as title, Discussion.date_created as date_created "
                "FROM Discussion WHERE Discussion.id=:id").params(id=discussion_id)
    discussion = db.engine.execute(stmt).fetchone()
    #print(str(comment))
    #discussion = Discussion.query.get(discussion_id)
    #messages = discussion.messages
    return render_template("discussions/discussion.html", comments=comments, discussion=discussion, form = CommentForm())



@app.route("/discussions/<discussion_id>", methods=["POST"])
@login_required
def discussions_comment(discussion_id):
    form = CommentForm(request.form)
    #TODO: validate input somehow
    message = Message(form.comment.data)
    message.set_account_id(current_user.id)
    message.set_discussion_id(discussion_id)
    
    db.session().add(message)
    db.session().commit()

    return redirect(url_for("discussions_show", discussion_id = discussion_id))


@app.route("/discussions/<discussion_id>", methods = ["DELETE"])
@login_required
def discussions_delete(discussion_id):
    
    discussion = Discussion.query.get(discussion_id)
    #only the user who created the discussion can delete it
    #TODO: also admin can remove any discussions
    if not discussion or discussion.account_id != current_user.id:
        return redirect(url_for("discussions_show", discussion_id = discussion_id))

    db.session().delete(discussion)
    db.session().commit()

    return redirect(url_for("discussions_index"))


    

