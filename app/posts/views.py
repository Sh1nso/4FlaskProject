from flask import Blueprint, render_template, request
from utils import *


post_blueprint = Blueprint('post_blueprint', __name__, template_folder='templates')


@post_blueprint.route('/posts/<post_id>')
def post_page(post_id):
    comments = CommentsDAO()
    post = PostsDAO()
    return render_template('post.html', post=post.get_post_by_pk(post_id),
                           comments=comments.get_comments_by_post_id(post_id),
                           length=len(comments.get_comments_by_post_id(post_id)))
