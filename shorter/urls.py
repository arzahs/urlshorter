from django.conf.urls import url
from shorter.views import CreateLink, LinkShow, RedirectLongLink


urlpatterns = [
    url(r'^$', CreateLink.as_view(), name='home'),
    url(r'^link/(?P<pk>\d+)$', LinkShow.as_view(), name='link_show'),
    url(r'^r/(?P<short_url>\w+)$', RedirectLongLink.as_view(), name='redirect')
]
