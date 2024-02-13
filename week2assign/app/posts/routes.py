from app.posts import postbp
from typing import Dict
from flask import jsonify, Response, request
import os
import json


@postbp.route('/posts', methods=["POST"])
def createPost() -> str:

    data = request.data

    writeFile(data)
    return "Your post has been recorded"

@postbp.route('/posts', methods=["GET"])
def getPosts() -> Response:
    file = os.getcwd()+"/app/posts/random_posts.txt"
    posts = read_posts(file)
    return jsonify(posts)

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

def read_posts(file: str | os.PathLike) -> Dict:
    posts: Dict = {}
    with open(file, "r") as f:
        temp: Dict ={}
        psts = 1
        for ln in f:
            if len(ln) > 1:
                if ln.startswith("Title"):
                    posts[psts] = temp
                    temp.clear()
                    psts += 1

                lns = ln.split(":", 1)
                temp[lns[0]] = lns[1].strip()
            else:
                continue
    return posts

def writeFile(data) -> None:
    data = json.loads(data)
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
