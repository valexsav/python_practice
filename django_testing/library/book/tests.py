from django.test import TestCase

from .models import Book
from author.models import Author


class LibraryTestCase(TestCase):

    def test_book_creation(self):
        Book.objects.create(
            title='The Great Gatsby',
            publication_year=1925,
            author=Author.objects.create(
                first_name='F. Scott',
                last_name='Fitzgerald',
                birth_date='1896-09-24',
            ),
        )

        self.assertTrue(Book.objects.filter(title='The Great Gatsby').exists())
        