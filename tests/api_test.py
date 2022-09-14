from main import app

keys_should_be_for_posts = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}


def test_api():
    response = app.test_client().get('/api/posts')

    assert type(response.json) == list, "Неверный тип данных"
    assert response.json[0].get("poster_name") == "leo", "Имя получено неверно"
    assert set(response.json[0].keys()) == keys_should_be_for_posts, "неверный список ключей"


def test_api_single_post():
    response = app.test_client().get('/api/posts/2')
    assert type(response.json) == dict, "Неверный тип данных"
    assert set(response.json.keys()) == keys_should_be_for_posts, "неверный список ключей"
