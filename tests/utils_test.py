from app.posts.posts_dao import PostsDAO
from app.comments.comments_dao import CommentsDAO
import pytest


@pytest.fixture()
def posts_dao():
    posts_dao_instance = PostsDAO()
    return posts_dao_instance


@pytest.fixture()
def comments_dao():
    comments_dao_instance = CommentsDAO()
    return comments_dao_instance


keys_should_be_for_posts = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}
keys_should_be_for_comments = {"post_id", "commenter_name", "comment", "pk"}


class TestPostsDAO:

    def test_get_posts_all(self, posts_dao):
        """ Check if the correct list of posts is returned """
        posts = posts_dao.get_posts_all()
        assert type(posts) == list, "возвращается не список"
        assert len(posts) > 0, "возвращается пустой список"
        assert set(posts[0].keys()) == keys_should_be_for_posts, "неверный список ключей"

    def test_get_by_pk(self, posts_dao):
        """ Checking if the correct post is returned when requesting one"""
        posts = posts_dao.get_post_by_pk(1)
        assert posts["pk"] == 1, "возвращается неправильный пост"
        assert set(posts.keys()) == keys_should_be_for_posts, "неверный список ключей"

    def test_get_posts_by_user(self, posts_dao):
        """
        Checking if the post is correct and returned when requested by the name of the commentator
        """
        posts = posts_dao.get_posts_by_user("leo")
        assert posts[0]["poster_name"] == "leo", "возвращается неправильный пост"
        assert set(posts[0].keys()) == keys_should_be_for_posts, "неверный список ключей"

    def test_search_for_posts(self, posts_dao):
        """
        Checking if the post is returned correctly when searching for the word
        """
        posts = posts_dao.search_for_posts("ага")
        assert posts[0]["content"] == "Ага, опять еда! Квадратная тарелка в квадратном кадре. А на тарелке, наверное," \
                                      " пирог! Мне было так жаль, что я не могу ее съесть. Я боялась, что они заметят, " \
                                      "и если я не съем это, то, значит, они все подумают, что я плохая девочка... " \
                                      "Но потом мне вспомнилось, как они на меня смотрели. Когда я была маленькой, " \
                                      "на кухне всегда были родители, бабушка, дедушка, дядя Борис... Все вместе. " \
                                      "И всегда одна я, потому что все остальные приходили туда лишь изредка. " \
                                      "Мне казалось, если бы все ходили на работу, как и я, в этот свой офис, " \
                                      "было бы совсем неинтересно.", "возвращается неправильный пост"
        assert set(posts[0].keys()) == keys_should_be_for_posts, "неверный список ключей"


class TestCommentsDAO:

    def test_get_comments_by_post_id(self, comments_dao):
        comments = comments_dao.get_comments_by_post_id(1)
        assert comments[0]["post_id"] == 1, "возвращается неправильный комментарий"
        assert set(comments[0].keys()) == keys_should_be_for_comments, "неверный список ключей"
