from django.db import models

# Create your models here.

class Link(models.Model):
    url = models.URLField()

    @staticmethod
    def shorter(link):
        l, _ = Link.objects.get_or_create(url=link.url)
        return str(l.pk)

    @staticmethod
    def expand(slug):
        l = Link.objects.get(pk=int(slug))
        return l.url
