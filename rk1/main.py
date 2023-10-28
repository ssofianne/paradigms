from operator import itemgetter


class Book:
    def __init__(self, id, title):
        self.title = title
        self.id = id


class Chapter:
    def __init__(self, chapter_id, name, pages, book_id):
        self.chapter_id = chapter_id
        self.name = name
        self.pages = pages
        self.book_id = book_id


class Chap_of_book:
    def __init__(self, book_id, chapter_id):
        self.book_id = book_id
        self.chapter_id = chapter_id


def build_relationships(books, chapters, chap_books):
    # Создаем отношение "один ко многим" 
    one_to_many = [(ch.name, ch.pages, b.title)
                   for b in books
                   for ch in chapters
                   if ch.book_id == b.id]

    # Создаем временное отношение "многие ко многим" 
    many_to_many_temp = [(b.title, chb.book_id, chb.chapter_id)
                         for b in books
                         for chb in chap_books
                         if b.id == chb.book_id]

    # Создаем отношение "многие ко многим" 
    many_to_many = [(ch.name, ch.pages, book_title)
                    for book_title, book_id, chapter_id in many_to_many_temp
                    for ch in chapters if ch.chapter_id == chapter_id]

    return one_to_many, many_to_many


# Задание А1:
def task_a1(one_to_many):
    res_11 = sorted(one_to_many, key=itemgetter(2))
    return res_11


# Задание А2:
def task_a2(books, one_to_many):
    res_12_unsorted = []
    # Перебираем все книги
    for b in books:
        # Список глав книги
        b_chps = list(filter(lambda i: i[2] == b.title, one_to_many))
        # Если книга с главами
        if len(b_chps) > 0:
            # Страницы глав этой книги
            b_pages = [pages for _, pages, _ in b_chps]
            # Общее количество страниц во всех главах книги
            b_pages_sum = sum(b_pages)
            res_12_unsorted.append((b.title, b_pages_sum))

    # Сортировка по суммарному количеству страниц
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    return res_12


# Задание А3:
def task_a3(books, many_to_many):
    res_13 = {}
    # Перебираем все книги
    for b in books:
        if 'Гарри Поттер' in b.title:
            # Список глав книги
            b_chps = list(filter(lambda i: i[2] == b.title, many_to_many))
            # Только названия глав
            b_chps_names = [x for x, _, _ in b_chps]
            # Добавляем результат в словарь
            # ключ - книга, значение - список глав
            res_13[b.title] = b_chps_names
    return res_13


def main():
    books = [
        Book(1, 'Город костей'),
        Book(2, 'Гарри Поттер от издательства N'),
        Book(3, 'Полианна'),
        Book(22, 'Гарри Поттер от издательства M'),
        Book(33, 'Гарри Поттер от издательства P'),
    ]

    chapters = [
        Chapter(1, 'Хранитель ключей', 21, 2),
        Chapter(2, 'Запретный лес', 17, 2),
        Chapter(3, 'Тайны и ложь', 5, 1),
        Chapter(4, 'Сумеречный охотник', 10, 1),
        Chapter(5, 'Мисс Полли', 6, 3)
    ]

    chap_books = [
        Chap_of_book(1, 3),
        Chap_of_book(1, 4),
        Chap_of_book(2, 1),
        Chap_of_book(2, 2),
        Chap_of_book(3, 5),

        Chap_of_book(22, 1),
        Chap_of_book(33, 2),
    ]

    one_to_many, many_to_many = build_relationships(books, chapters, chap_books)

    print('\nЗадание А1:')
    res_11 = task_a1(one_to_many)
    for item in res_11:
        print(item)

    print('\nЗадание А2:')
    res_12 = task_a2(books, one_to_many)
    for item in res_12:
        print(item)

    print('\nЗадание А3:')
    res_13 = task_a3(books, many_to_many)
    for key, value in res_13.items():
        print(f'{key}: {value}')


if __name__ == '__main__':
    main()
