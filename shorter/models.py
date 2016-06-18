from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.


class Link(models.Model):
    url = models.URLField()

    def get_absolute_url(self):
        return reverse("shorter:link_show", kwargs={"pk": self.pk})

    @staticmethod
    def shorter(link):
        l, _ = Link.objects.get_or_create(url=link.url)
        return str(l.pk)

    @staticmethod
    def expand(slug):
        l = Link.objects.get(pk=int(slug))
        return l.url
