from django.test import TestCase

from .models import Book, Category


class RandomTestCase(TestCase):
    def setUp(self):
        self.a = 2

    def tearDown(self):
        del self.a

    def test_a_is_2(self):
        self.assertEqual(self.a, 2)


class CategoryTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="test",)

    def tearDown(self):
        del self.category

    def test_category_instance(self):
        self.assertIsInstance(self.category, Category)


class BookTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="test", )
        self.book = Book.objects.create(title="Python", author="James", category=self.category)

    def tearDown(self):
        del self.category
        del self.book

    def test_book_instance(self):
        self.assertIsInstance(self.book, Book)

    def test_category_field(self):
        self.assertIsInstance(self.book.category, Category)

    def test_book_attributes(self):
        self.assertEqual(self.book.title, 'Python')
        self.assertEqual(self.book.author, 'James')

    def test_string_representation(self):
        self.assertEqual(str(self.book), 'Python by James')
