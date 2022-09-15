import json


class BookmarkDAO:
    def __init__(self):
        self.path = 'data/bookmarks.json'

    def load_posts_from_data(self) -> list:
        """
        Load data from file
        """
        with open(self.path, encoding='utf-8') as file:
            data = json.load(file)
        return data

    def get_post_by_pk(self, pk) -> [dict, str]:
        for post in self.load_posts_from_data():
            if post['pk'] == int(pk):
                return post
        return f'Ошибка pk'