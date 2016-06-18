from django.test import TestCase
from shorter.models import Link
# Create your tests here.


class ShorterTest(TestCase):

    def test_shorter(self):
        url = 'http://testing_long.url/test'
        link = Link(url=url)
        short_link = Link.shorter(link)
        self.assertLess(len(short_link), len(url))

    def test_expand(self):
        url = 'http://testing_long.url/test'
        link = Link(url=url)
        short_link = Link.shorter(link)
        link.save()
        expand_url = Link.expand(short_link)
        self.assertEqual(expand_url, url)




