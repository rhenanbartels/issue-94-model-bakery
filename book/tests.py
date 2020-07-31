from django.conf import settings
from django.test import TestCase
from model_bakery import baker

from book.models import Author, BookCopy


class TestBookAuthorship(TestCase):
    databases = settings.DATABASES

    def test_let_model_bakery_create_related_field(self):
        book_copy = baker.make(BookCopy, _save_kwargs={"using": "hr_db"})

        self.assertEqual(book_copy.author.id, Author.objects.last().id)

    def test_create_book_and_its_authors_both_setting_database(self):
        author = baker.make(Author, _save_kwargs={"using": "hr_db"})
        book_copy = baker.make(
            BookCopy,
            author=author,
            _save_kwargs={"using": "hr_db"}
        )

        self.assertEqual(Author.objects.using("hr_db").last().id, author.id)
        self.assertEqual(
            Author.objects.using("hr_db").last().id, book_copy.author.id
        )

    def test_create_book_and_its_authors_both_default_database(self):
        book_copy = baker.make(BookCopy)

        self.assertEqual(book_copy.author.id, Author.objects.last().id)
