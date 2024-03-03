from app.posts import postbp
from typing import Dict
from flask import render_template, redirect, Response, flash
from flask_login import login_required, current_user
import os, json
from datetime import datetime
from .forms import PostFrom
from .models import BlogPost
from app import get_db
from app.users.models import User

db = get_db()

@postbp.route('', methods=["GET"])
def getPosts() -> str:
    posts = BlogPost.query.all()
    return render_template("/posts/posts.html", data=posts)


@postbp.route('create', methods=["GET", "POST"])
@login_required
def createPost():
    form = PostFrom()
    user_id = current_user.get_id()
    user = User.query.filter_by(id=user_id).first()
    if form.validate_on_submit() and current_user.is_authenticated:
        new_post = BlogPost(
            title = form.title.data,
            body = form.description.data,
            author = user,
            created_at = datetime.now(),
            updated_at = datetime.now()
        )
        db.session.add(new_post)
        db.session.commit()
        flash('Success.')
        return redirect("/posts")
  
    return render_template("/posts/createpost.html", form=form)

@postbp.route('<int:post_id>', methods=["GET"])
def getPost(post_id) -> str:
    post = BlogPost.query.filter_by(id=post_id).first_or_404()
    return render_template("/posts/post.html", data=post)

@postbp.route('/posts/delete/<int:post_id>', methods=["GET", "DELETE"])
@login_required
def deletePost(post_id) -> Response:
    BlogPost.query.filter_by(id=post_id).delete()
    db.session.commit()
    return redirect("/posts")