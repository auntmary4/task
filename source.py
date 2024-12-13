import datetime
import json
import random

_DOWNLOAD_PATH = "Download/" 
_N = 0

class Article:
    def __init__(self, title, author, content):
        self.title = title
        self.author = author
        self.content = content
        self.likes = random.randint(0, 100)
        self.creation_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def generate_random_title():
    """Генерирует случайное название статьи из предустановленных шаблонов."""
    templates = [
        "Как {verb} {noun}",
        "Топ 10 {noun}",
        "Почему {noun} важен",
        "Лучшие советы по {noun}",
        "Будущее {noun}: что ожидать",
    ]
    nouns = ["технологии", "инновации", "наука", "бизнес", "образование"]
    verbs = ["улучшить", "использовать", "изучить", "развивать", "практиковать"]
    
    template = random.choice(templates)
    title = template.format(
        noun=random.choice(nouns),
        verb=random.choice(verbs)
    )
    return title

def json_dump_article(art: Article):
    global _N
    _N += 1
    dt = datetime.datetime.now()
    dt_str = dt.strftime('%Y-%m-%d_%H-%M-%S') 
    path = f'{_DOWNLOAD_PATH}{_N}_{dt_str}.json'
    
    # Открываем файл с указанием кодировки utf-8
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(art.__dict__, f, ensure_ascii=False)

def get_article():
    title = generate_random_title()
    author = f"Автор {random.randint(1, 100)}"
    content = f"Это содержание статьи с заголовком '{title}'."
    art = Article(title, author, content)
    return art

def do_work():
    art = get_article()
    json_dump_article(art)

# Создание и сохранение 10 статей
for _ in range(10):
    do_work()

print('Успешно выполнено!')