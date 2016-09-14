from django.test import TestCase


class RandomTestCase(TestCase):
    def setUp(self):
        self.a = 2

    def tearDown(self):
        del self.a

    def test_a_is_2(self):
        self.assertEqual(self.a, 2)
