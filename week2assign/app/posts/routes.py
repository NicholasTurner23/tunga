from app.posts import postbp
from typing import Dict
from flask import request, render_template, redirect, Response, flash
import os, json
from datetime import datetime
from .forms import PostFrom
from .models import BlogPost
from app import get_db

db = get_db()
@postbp.route('/posts/create', methods=["GET", "POST"])
def createPost():
    form = PostFrom()
    if form.validate_on_submit():
        new_post = BlogPost(
            title = form.title.data,
            body = form.description.data,
            author = form.author.data,
            created_at = datetime.now(),
            updated_at = datetime.now()
        )
        db.session.add(new_post)
        db.session.commit()
        flash('Success.')
        return redirect("/posts")
  
    return render_template("createpost.html", form=form)

@postbp.route('/posts/<int:post_id>', methods=["GET"])
def getPost(post_id) -> str:
    post = BlogPost.query.filter_by(id=post_id).first_or_404()
    return render_template("post.html", data=post)

@postbp.route('/posts', methods=["GET"])
def getPosts() -> str:
    posts = BlogPost.query.all()
    return render_template("posts.html", data=posts)

@postbp.route('/posts/delete/<int:post_id>', methods=["POST", "DELETE"])
def deletePost(post_id) -> Response:
    BlogPost.query.filter_by(id=post_id).delete()
    db.session.commit()
    return redirect("/posts")


def read_posts(file: str | os.PathLike) -> list:
    posts: list = []
    with open(file, "r") as f:
        temp: Dict ={}
        for ln in f:
            if len(ln) > 1:
                if ln.startswith("Title") and len(temp) > 0:
                    posts.append(temp.copy())
                    temp.clear()
                lns = ln.split(":", 1)
                temp[lns[0]] = lns[1].strip()
            else:
                continue
    return posts

def writeFile(data) -> None:
    # data = json.loads(data)
    path = os.getcwd()+"/app/posts/random_posts.txt"
    file = open(path, "a")
    file.write("Title: {}\n".format(data["title"]))
    file.write("Description: {}\n".format(data["description"]))
    file.write("Author: {}\n".format(data["author"]))
    file.write("Date Posted: {}\n".format(data["date_posted"]))
    file.write("Date Updated: {}\n".format(data["date_updated"]))
    file.write("Views: {}\n".format(data["views"]))
    file.write("Likes: {}\n".format(data["likes"]))
    file.write("\n")
    file.close()
