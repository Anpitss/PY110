import json
import re

BOOK_JSON = "books.json"
BOOKS_FILE = "books.md"
BOOK_REGEX = r'#{4}\s(?P<position>\d+)\.\s\[(?P<book>.+?)\]\((?P<book_url>.+?)\)\s+by\s(?P<author>.+?)\s\((?P<recommended>.+?\%) recommended\).+?\((?P<cover_url>.+?)\).+?\"(?P<description>.+?)\"'  # TODO записать ругулярное выражения для поиска книги


def task():
    book_pattern = re.compile(BOOK_REGEX, re.DOTALL)  # флаг re.DOTALL описывает, что под символом точка может содержаться символ переноса строки
    dict_ = []
    with open(BOOKS_FILE) as f:
        for book in book_pattern.finditer(f.read()):
            print(json.dumps(book.groupdict(), indent=4))
            dict_.append(book.groupdict())
        dict_.sort(key=lambda x: x['recommended'])

    with open(BOOK_JSON, 'w', encoding='utf-8') as f:
        json.dump(dict_, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    task()
