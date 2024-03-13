from flask import request, jsonify
from app.posts.models import  BlogPost, blogposts_schema, blogpost_schema
from flask_restful import Resource
from app import get_db

db = get_db()
class BlogPostsApi(Resource):
    def get(self):
        posts = BlogPost.query.all()
        posts = blogposts_schema.dump(posts)
        if not posts:
            return jsonify({'info': 'No Posts found'}), 200
        return posts, 200
    
    def post(self):
        post_args = request.get_json()
        posts = blogpost_schema.load(post_args, session=db.session)
        db.session.add(posts)
        db.session.commit()
        return blogpost_schema.dump(posts), 201
    
class BlogPostApi(Resource):
    def get(self, post_id):
        post = BlogPost.query.filter_by(id=post_id).first_or_404()
        if not post:
            return jsonify({'error': 'The object you are looking for does not exist'}), 400
        return blogpost_schema.dump(post), 200
    
    def put(self, post_id):
        post_args = request.json
        post = BlogPost.query.filter_by(id=post_id).first_or_404()
        post.title = post_args['title']
        post.body = post_args['body']
        db.session.commit()
        return blogpost_schema.dump(post), 200
    
    def delete(self, post_id):

        post = BlogPost.query.filter_by(id=post_id)
        if post:
            post.delete()
        else:
            return jsonify({'error': 'The object you are looking for does not exist'}), 400
        db.session.commit()
        return blogpost_schema.dump(post), 200