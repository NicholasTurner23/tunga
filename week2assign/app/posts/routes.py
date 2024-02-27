from app.posts import postbp
from typing import Dict
from flask import request, render_template, redirect
import os, json
from datetime import datetime
from .forms import PostFrom


@postbp.route('/posts/create', methods=["GET", "POST"])
def createPost():
    # data = request.data
    data = {}
    form = PostFrom()
    if form.validate_on_submit():
        data["title"] = form.title.data
        data["description"] = form.description.data
        data["author"] = form.author.data
        data["views"] = 0
        data["likes"] = 0
        data["date_posted"] = datetime.now()
        data["date_updated"] = datetime.now()

    if data:
        writeFile(data)
        data.clear()
        return redirect("/posts")
    return render_template("createpost.html", form=form)

@postbp.route('/posts', methods=["GET"])
def getPosts() -> str:
    file = os.getcwd()+"/app/posts/random_posts.txt"
    posts = read_posts(file)
    return render_template("posts.html", data=posts)

@postbp.route('/posts/<int:post_id>', methods=["GET"])
def getPost(post_id) -> str:
    return f"Work in progres - One post - {post_id}"

@postbp.route('/posts/<int:post_id>', methods=["DELETE"])
def deletePost(post_id) -> str:
    return f"Work in progres - delete - {post_id}"

@postbp.route('/posts/<int:post_id>', methods=["PUT"])
def updatePost(post_id) -> str:
    return f"Work in progres - Update - {post_id}"

@postbp.route('/posts/<int:post_id>', methods=["PATCH"])
def patchPost(post_id) -> str:
    return f"Work in progres - Patch - {post_id}"

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
