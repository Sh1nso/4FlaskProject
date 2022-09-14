import json


class CommentsDAO:
    def __init__(self):
        self.path = 'data/comments.json'

    def load_comments_from_data(self) -> list[dict]:
        """
        Load comments from file
        """
        with open(self.path, encoding='utf-8') as file:
            data = json.load(file)
        return data

    def get_comments_by_post_id(self, post_id: str) -> list:
        """
        Return comments by post_id.
        Return blank list if post hasn't comments
        """
        comments_by_dost_id = []
        try:
            for comment in self.load_comments_from_data():
                if comment['post_id'] == int(post_id):
                    comments_by_dost_id.append(comment)
            return comments_by_dost_id
        except ValueError:
            f'Такого поста нет'
        return comments_by_dost_id
