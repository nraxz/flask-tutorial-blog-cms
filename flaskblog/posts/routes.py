# /flaskblog/posts/routes.py

from flask import Blueprint, request
from flaskblog.posts.controllers.post_controller import (
    new_post_controller, post_controller, update_post_controller, delete_post_controller
)
from flask_login import login_required

posts = Blueprint('posts', __name__)

@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    return new_post_controller()

@posts.route("/post/<int:post_id>")
def post(post_id):
    return post_controller(post_id)

@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    return update_post_controller(post_id)

@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    return delete_post_controller(post_id)
