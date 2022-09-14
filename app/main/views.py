from flask import Blueprint, render_template, request
from app.posts.posts_dao import PostsDAO

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def page_index():
    data = PostsDAO()
    return render_template('index.html', context=data.get_posts_all())


@main_blueprint.route('/search')
def search_post_by_word():
    post_dao = PostsDAO()
    s = request.args['s']
    post_by_word = post_dao.search_for_posts(s)
    return render_template('search.html', posts=post_by_word, length=len(post_by_word))


@main_blueprint.route('/users/<username>')
def get_by_user(username):
    post_dao = PostsDAO()
    posts_by_user_name = post_dao.get_posts_by_user(username)
    return render_template('user-feed.html', posts=posts_by_user_name)

