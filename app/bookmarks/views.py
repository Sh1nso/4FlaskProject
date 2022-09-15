from flask import Blueprint, redirect, render_template
from app.posts.posts_dao import PostsDAO
from utils import append_post_to_data, remove_post_from_data
from app.bookmarks.bookmarks_dao import BookmarkDAO

bookmarks_blueprint = Blueprint('bookmarks_blueprint', __name__, template_folder='templates')


@bookmarks_blueprint.route('/bookmarks')
def get_bookmarks():
    bookmarks = BookmarkDAO()
    return render_template('bookmarks.html', posts=bookmarks.load_posts_from_data())


@bookmarks_blueprint.route('/bookmarks/add/<post_id>')
def add_post_to_bookmarks(post_id):
    post = PostsDAO()
    bookmarks = BookmarkDAO()
    post_by_id = post.get_post_by_pk(post_id)
    if post_by_id not in bookmarks.load_posts_from_data():
        append_post_to_data(post_by_id)
        return redirect('/bookmarks', code=302)
    return redirect('/bookmarks', code=302)


@bookmarks_blueprint.route('/bookmarks/remove/<post_id>')
def delete_post_from_bookmarks(post_id):
    bookmarks = BookmarkDAO()
    bookmark_by_id = bookmarks.get_post_by_pk(post_id)
    remove_post_from_data(bookmark_by_id)
    return redirect('/bookmarks', code=302)
