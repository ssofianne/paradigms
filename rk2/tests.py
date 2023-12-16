import unittest
from main import *
class Test_Program(unittest.TestCase):
    # Глобальные переменные
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

    def test_A1(self):
        one_to_many = [(ch.name, ch.pages, b.title)
                       for b in self.books
                       for ch in self.chapters
                       if ch.book_id == b.id]

        self.assertEqual(a1_solution(one_to_many),
                         [('Хранитель ключей', 21, 'Гарри Поттер от издательства N'),
                          ('Запретный лес', 17, 'Гарри Поттер от издательства N'),
                          ('Тайны и ложь', 5, 'Город костей'),
                          ('Сумеречный охотник', 10, 'Город костей'),
                          ('Мисс Полли', 6, 'Полианна')])

    def test_A2(self):
        one_to_many = [(ch.name, ch.pages, b.title)
                       for b in self.books
                       for ch in self.chapters
                       if ch.book_id == b.id]

        self.assertEqual(a2_solution(one_to_many, self.books),
                         [('Гарри Поттер от издательства N', 38),
                          ('Город костей', 15),
                          ('Полианна', 6)])

    def test_A3(self):
        many_to_many_temp = [(b.title, chb.book_id, chb.chapter_id)
                             for chb in self.chap_books
                             for b in self.books
                             if b.id == chb.book_id]

        many_to_many = [(ch.name, ch.pages, book_title)
                        for book_title, book_id, chapter_id in many_to_many_temp
                        for ch in self.chapters if ch.chapter_id == chapter_id]

        self.assertDictEqual(a3_solution(many_to_many, self.books),{'Гарри Поттер от издательства N': ['Хранитель ключей', 'Запретный лес'],
                                                        'Гарри Поттер от издательства M': ['Хранитель ключей'],
                                                        'Гарри Поттер от издательства P': ['Запретный лес']})


if __name__ == '__main__':
    unittest.main()