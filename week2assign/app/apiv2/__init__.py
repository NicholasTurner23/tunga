from flask import Blueprint
from flask_restful import Api

apibp2 = Blueprint('api2', __name__)
api = Api(apibp2)


# def initialize_routes(api):
#     from . import posts_resource
#     api.add_resource(posts_resource.BlogPostApi, '/api/post/<int:post_id>', endpoint="api/post")
#     api.add_resource(posts_resource.BlogPostsApi, '/api/posts', endpoint="api/posts")

from app.apiv2 import posts_resource

api.add_resource(posts_resource.BlogPostApi, '/post/<int:post_id>')
api.add_resource(posts_resource.BlogPostsApi, '/posts')