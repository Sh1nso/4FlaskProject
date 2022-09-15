import json


def append_post_to_data(some_post: dict):
    """
    Добавляет данные о посте пользователя в JSON файл и перезаписывает его
    """
    try:
        with open("data/bookmarks.json", 'r', encoding='utf-8') as file:
            data = json.loads(file.read())
            data.append(some_post)
        with open("data/bookmarks.json", 'w', encoding='utf-8') as file1:
            json.dump(data, file1, ensure_ascii=False)
    except FileNotFoundError:
        return f'Файл не найден'
    except json.JSONDecodeError:
        return f'Файл не удается преобразовать'


def remove_post_from_data(some_post: dict):
    """
    Добавляет данные о посте пользователя в JSON файл и перезаписывает его
    """
    try:
        with open("data/bookmarks.json", 'r', encoding='utf-8') as file:
            data = json.loads(file.read())
            data.remove(some_post)
        with open("data/bookmarks.json", 'w', encoding='utf-8') as file1:
            json.dump(data, file1, ensure_ascii=False)
    except FileNotFoundError:
        return f'Файл не найден'
    except json.JSONDecodeError:
        return f'Файл не удается преобразовать'
