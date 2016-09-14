from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from .models import Book, Category
from .views import HomePageView


class RandomTestCase(TestCase):
    def setUp(self):
        self.a = 2

    def tearDown(self):
        del self.a

    def test_a_is_2(self):
        self.assertEqual(self.a, 2)


class CategoryTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="test")

    def tearDown(self):
        del self

    def test_category_instance(self):
        self.assertIsInstance(self.category, Category)

    def test_string_representation(self):
        self.assertEqual(str(self.category.name), 'test')


class BookTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="test", )
        self.book = Book.objects.create(title="Python", author="James", category=self.category)

    def tearDown(self):
        del self

    def test_book_instance(self):
        self.assertIsInstance(self.book, Book)

    def test_category_field(self):
        self.assertIsInstance(self.book.category, Category)

    def test_book_attributes(self):
        self.assertEqual(self.book.title, 'Python')
        self.assertEqual(self.book.author, 'James')

    def test_string_representation(self):
        self.assertEqual(str(self.book), 'Python by James')


class HomePageTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name="test")
        self.book1 = Book.objects.create(title="Python", author="James", category=self.category)
        self.book2 = Book.objects.create(title="ES6", author="No name", category=self.category)

    def tearDown(self):
        del self

    def test_home_page_get_response(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_post_response(self):
        response = self.client.post(reverse('home'), data=dict(search_term='phone'))
        self.assertEqual(response.status_code, 200)

    def test_category_matches_are_found(self):
        matches = HomePageView.get_category_matches(Book, 'est')
        self.assertEqual(len(matches), 2)

    def test_book_title_match_is_found(self):
        matches = HomePageView.get_book_title_matches(Book, 'tho')
        self.assertEqual(len(matches), 1)
