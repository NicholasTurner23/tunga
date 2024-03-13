from flask import request, jsonify
from typing import List, TypeVar, Union
from app import get_db
from app.posts.models import  BlogPost, blogpost_schema
from app.api import apibp

T =TypeVar('T')
db = get_db()
ListOrPost = Union[List, BlogPost]
@apibp.route('/posts', methods=["POST"])
def createPost():
    post_args = request.get_json()
    posts = blogpost_schema.load(post_args, session=db.session)
    db.session.add(posts)
    db.session.commit()
    return blogpost_schema.dump(posts), 201


@apibp.route('/post/<int:post_id>', methods=["GET"])
def getpost(post_id):
    post = BlogPost.query.filter_by(id=post_id).first_or_404()
    post_data = data_helper(post)
    return jsonify(post_data)


@apibp.route('/posts', methods=["GET"])
def getposts():
    posts = BlogPost.query.all()
    posts_data = data_helper(posts)
    return jsonify(posts_data)


def data_helper(posts:ListOrPost) -> List:
    if isinstance(posts, list):
        posts_data = [{'id': post.id, 'title': post.title, 'body': post.body, 'author':post.author.username, 'created_at': post.created_at.strftime('%Y-%m-%d %H:%M:%S.%f')} for post in posts]
    else:
        posts_data = [{'id': posts.id, 'title': posts.title, 'body': posts.body, 'author':posts.author.username, 'created_at': posts.created_at.strftime('%Y-%m-%d %H:%M:%S.%f')}]
    return posts_data
