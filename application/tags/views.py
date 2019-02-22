from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.sql import text
from application import app, db
from application.auth.models import User
from application.discussions.models import Discussion, discussion_tag
from application.tags.models import Tag
from application.messages.models import Message
from application.discussions.forms import DiscussionForm, CommentForm
from application.tags.forms import SearchTagForm

# Find discussions by their tags and their title
@app.route("/tags/search", methods=["POST"])
def find_discussions_with_tag():
    form = SearchTagForm(request.form)
    #remove whitespace from beginning and end of string
    tagname=form.tags.data.strip()

    # Use this as parameter for sql search to find any tags which contains given parameter, e.g search any tag with 'ta' in it.
    name='%' + tagname + '%'
    stmt=text(" SELECT account.id as account_id, account.username, discussion.id, discussion.date_created, discussion.date_modified, discussion.title "
                "FROM account INNER JOIN discussion on  account.id=discussion.account_id WHERE discussion.id IN"
                "(SELECT distinct discussion.id from discussion "
                "INNER JOIN discussion_tag ON discussion.id=discussion_tag.discussion_id "
                "INNER JOIN tag on discussion_tag.tag_id=tag.id "
                "WHERE tag.name LIKE :name) ").params(name=name)
    discussions_by_tag=db.engine.execute(stmt)

    stmt=text("SELECT account.id as account_id, Account.username, discussion.id, discussion.date_created, discussion.date_modified, discussion.title "
                "FROM Account INNER JOIN discussion ON account.id=discussion.account_id WHERE discussion.title LIKE :name").params(name=name)
    discussions_by_title = db.engine.execute(stmt)


    return render_template("tags/list.html", discussions_by_tag=discussions_by_tag, discussions_by_title=discussions_by_title, tag=tagname, searchform=SearchTagForm())
