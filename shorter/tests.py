from django.test import TestCase
from django.core.urlresolvers import reverse
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

    def test_homepage(self):
        response = self.client.get(reverse("shorter:home"))
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)

    def test_shorter_form(self):

        url = "http://example.com/"
        response = self.client.post(reverse("shorter:home"),
                                    {"url": url}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn("link", response.context)
        link = response.context['link']
        short_url = Link.shorter(link)
        self.assertEqual(url, link.url)
        self.assertIn(short_url, response.content.decode('utf8'))

    def test_redirect_to_long_url(self):
        url = "http://example.com/"
        link = Link.objects.create(url=url)
        short_link = Link.shorter(link)
        response = self.client.get(reverse("shorter:redirect",
                                           kwargs={'short_url': short_link})
                                   )
        self.assertRedirects(response, url)






