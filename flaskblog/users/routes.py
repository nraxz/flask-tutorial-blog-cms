from flask import Blueprint
from flask_login import login_required
from flaskblog.users.controllers.user_controller import (register_user, login_user_custom,
                                                         logout_controller, account_controller, user_posts_get,
                                                         reset_request, reset_token)

users = Blueprint('users', __name__)

@users.route("/register", methods=['GET', 'POST'])
def register():
    return register_user()

@users.route("/login", methods=['GET', 'POST'])
def login():
    return login_user_custom()

@users.route("/logout")
def logout():
    return logout_controller()

@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    return account_controller()

@users.route("/user/<string:username>")
def user_posts(username):
    return user_posts_get(username)

@users.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    return reset_request()

@users.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    return reset_token(token)
