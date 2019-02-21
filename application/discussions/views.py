from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.sql import text
from application import app, db
from application.auth.models import User
from application.discussions.models import Discussion
from application.tags.models import Tag
from application.messages.models import Message
from application.discussions.forms import DiscussionForm, CommentForm
from application.tags.forms import SearchTagForm

@app.route("/")
def index():
    return redirect(url_for("discussions_index"))

@app.route("/discussions", methods=["GET"])
def discussions_index(success=None):
    stmt = text("SELECT account.username as username, discussion.id as d_id, "
                "discussion.account_id as a_id, Discussion.title as title, discussion.date_created as d_date_created, "
                "COUNT(message.id) as totalmessages, MAX(message.date_created) as latest_message "
                "FROM account INNER JOIN discussion ON discussion.account_id=account.id "
                "LEFT JOIN message ON message.discussion_id=discussion.id "
                "GROUP BY discussion.title, account.username, discussion.id ORDER BY latest_message DESC")
    discussions = db.engine.execute(stmt)
    if(success is not None):
        return render_template("discussions/list.html", discussions=discussions, success=success, searchform=SearchTagForm())
    else:
        return render_template("discussions/list.html", discussions=discussions, searchform=SearchTagForm())

@app.route("/discussions/new")
@login_required
def discussions_form():
    return render_template("discussions/new.html", form = DiscussionForm(), searchform=SearchTagForm())


@app.route("/discussions", methods=["POST"])
@login_required
def discussions_create():
    form = DiscussionForm(request.form)
    if not form.validate():
        return render_template("discussions/new.html", form=DiscussionForm(), error = "Title length must be between 5 and 100 characters. Content must be between 5 and 2000 characters.")
    discussion = Discussion(form.title.data)
    discussion.set_account_id(current_user.id)
    discussion_tags=form.tags.data.split(' ')
    for tagname in discussion_tags:
        # Check for empty strings
        if tagname and tagname.strip():
            tag=Tag(tagname)
            discussion.tags.append(tag)
    db.session().add(discussion)
    db.session().commit()


    message = Message(form.content.data)
    message.set_account_id(current_user.id)
    message.set_discussion_id(discussion.id)

    db.session().add(message)
    db.session().commit()

    return redirect(url_for("discussions_show", discussion_id = discussion.id))


@app.route("/discussions/<discussion_id>", methods=["GET"])
def discussions_show(discussion_id):
    stmt = text("SELECT Account.username AS account_username, "
                "Account.date_created AS account_date_created, "
                "Message.content AS message_content, "
                "Message.date_created AS message_date_created,  "
                "Message.date_modified AS message_date_modified, "
                "Message.account_id as a_id, Message.id as m_id "
                "FROM Account, Message, Discussion WHERE Account.id = Message.account_id "
                "AND Discussion.id = Message.discussion_id " 
                "AND Discussion.id = :id").params(id = discussion_id)

    comments = db.engine.execute(stmt)
    stmt = text("SELECT Discussion.id AS id, Discussion.title as title, Discussion.date_created as date_created "
                "FROM Discussion WHERE Discussion.id=:id").params(id=discussion_id)
    discussion = db.engine.execute(stmt).fetchone()

    stmt=text("select tag.name from discussion, tag, discussion_tag "
            "WHERE discussion.id = discussion_tag.discussion_id "
            "AND tag.id = discussion_tag.tag_id "
            "AND discussion_id= :id").params(id = discussion_id)
    tags = db.engine.execute(stmt)

    #print(str(comment))
    #discussion = Discussion.query.get(discussion_id)
    #messages = discussion.messages
    return render_template("discussions/discussion.html", comments=comments, discussion=discussion, form = CommentForm(), tags=tags)



@app.route("/discussions/<discussion_id>", methods=["POST"])
@login_required
def discussions_comment(discussion_id):
    form = CommentForm(request.form)
    if not form.validate():
        return redirect(url_for("discussions_show", discussion_id = discussion_id))
    message = Message(form.comment.data)
    message.set_account_id(current_user.id)
    message.set_discussion_id(discussion_id)
    
    db.session().add(message)
    db.session().commit()

    return redirect(url_for("discussions_show", discussion_id = discussion_id))


@app.route("/discussions/<discussion_id>/delete", methods = ["POST"])
@login_required
def discussions_delete(discussion_id):
    
    discussion = Discussion.query.get(discussion_id)
    # Get current user's role from database
    check_admin_user=User.query.get(current_user.id)
    # If discussion does not exist or user deleting it is not the creator of the discussion and is not admin, redirect back.
    if not discussion or discussion.account_id != current_user.id and check_admin_user.role != 'admin':
            return redirect(url_for("discussions_show", discussion_id = discussion_id))
    

    # Delete messages related to discussion

    stmt = text("DELETE FROM Message WHERE Message.discussion_id=:id").params(id=discussion_id)
    db.engine.execute(stmt)

    # Delete discussion

    #TODO: When tags exist, delete them here

    db.session().delete(discussion)
    db.session().commit()

    return redirect(url_for("discussions_index", success="Discussion successfully deleted."))


@app.route("/discussions/<discussion_id>/<message_id>/delete", methods=["POST"])
@login_required
def discussions_delete_message(discussion_id, message_id):
    message = Message.query.get(message_id)
    check_admin_user=User.query.get(current_user.id)
    # If message does not exist or message not sent by current user and current user is not admin or message discussion id is wrong, redirect back
    if not message or message.account_id != current_user.id and check_admin_user.role!='admin' or message.discussion_id != int(discussion_id):
        return redirect(url_for('discussions_show', discussion_id = discussion_id, searchform=SearchTagForm()))
    
    db.session().delete(message)
    db.session().commit()

    return redirect(url_for('discussions_show', discussion_id = discussion_id))


@app.route("/discussions/<discussion_id>/<message_id>/edit", methods=["POST"])
@login_required
def discussions_edit_message(discussion_id, message_id):
    message=Message.query.get(message_id)
    if not message or message.account_id != current_user.id:
        return redirect(url_for('discussions_index'))
    form = CommentForm(request.form)
    if not form.validate():
        return redirect(url_for('discussions_index'))
    message.content = form.comment.data
    
    db.session().commit()
    return redirect(url_for('discussions_show', discussion_id = discussion_id))

@app.route("/discussions/<discussion_id>/<message_id>/edit", methods=["GET"])
@login_required
def discussions_edit_message_page(discussion_id, message_id):
    message=Message.query.get(message_id)
    if message.account_id != current_user.id:
        return redirect(url_for('discussions_index'))
    return render_template("discussions/editmessage.html", message=message, form=CommentForm(), discussion_id=discussion_id)




    

