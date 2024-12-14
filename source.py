import datetime
import json
import random
import os

# Путь для сохранения файлов
_DOWNLOAD_PATH = "Download/"
_N = 0

class Article:
    def __init__(self, name):
        """Класс для представления статьи."""
        self.name = name
        self.likes = random.randint(0, 100)


def ensure_directory_exists(path):
    """Проверяет существование директории и создает её, если нужно."""
    if not os.path.exists(path):
        os.makedirs(path)


def json_dump_article(art: Article):
    """Сохраняет объект статьи в файл JSON."""
    global _N
    _N += 1

    # Генерация имени файла с отметкой времени
    dt = datetime.datetime.now()
    dt_str = dt.strftime('%Y-%m-%d_%H-%M-%S')
    path = f'{_DOWNLOAD_PATH}{_N}_{dt_str}.json'

    # Убедиться, что директория существует
    ensure_directory_exists(_DOWNLOAD_PATH)

    try:
        with open(path, 'w') as f:
            json.dump(art.__dict__, f, indent=4)  # Добавлен параметр indent для читаемости
    except Exception as e:
        print(f"Ошибка при записи файла {path}: {e}")


def get_article():
    """Создает новую статью."""
    return Article(f"Article {random.randint(1000, 9999)}")


def do_work():
    """Создает статью и сохраняет её в файл."""
    art = get_article()
    json_dump_article(art)


if __name__ == "__main__":
    # Основной цикл работы
    for i in range(10):
        do_work()

    print('Все статьи успешно сохранены!')
