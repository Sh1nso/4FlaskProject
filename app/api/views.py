from flask import Blueprint, jsonify
from app.posts.posts_dao import PostsDAO
import logging

new_logger = logging.getLogger()

formatter_one = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
file_handler = logging.FileHandler("api.log")
file_handler.setFormatter(formatter_one)

new_logger.addHandler(file_handler)

api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route('/api/posts')
def get_posts_for_api():
    data = PostsDAO()
    post_data = data.get_posts_all()
    new_logger.info(f'Запрос получения постов')
    return jsonify(post_data)


@api_blueprint.route('/api/posts/<post_id>')
def get_one_post_for_api(post_id):
    data = PostsDAO()
    post_data = data.get_post_by_pk(post_id)
    new_logger.info(f'Запрос получения поста под номером {post_id}')
    return jsonify(post_data)



