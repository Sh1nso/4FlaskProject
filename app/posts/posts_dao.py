import json


class PostsDAO:
    def __init__(self):
        self.path = 'data/posts.json'

    def load_posts_from_data(self) -> list:
        """
        Load data from file
        """
        with open(self.path, encoding='utf-8') as file:
            data = json.load(file)
        return data

    def get_posts_all(self):
        """Return list of all posts"""
        posts = self.load_posts_from_data()
        return posts

    def get_posts_by_user(self, user_name: str) -> list:
        """
        Return list of posts by username, or blank list if user_name hasn't posts
        """
        list_of_posts_by_user_name = []
        for post in self.load_posts_from_data():
            if post['poster_name'] == user_name:
                list_of_posts_by_user_name.append(post)
        return list_of_posts_by_user_name

    def search_for_posts(self, query: str) -> list:
        """
        Return posts by query
        """
        list_of_posts_by_query = []
        for post in self.load_posts_from_data():
            if query.lower() in post['content'].lower():
                list_of_posts_by_query.append(post)
        return list_of_posts_by_query

    def get_post_by_pk(self, pk) -> [dict, str]:
        for post in self.load_posts_from_data():
            if post['pk'] == int(pk):
                return post
        return f'Ошибка pk'
