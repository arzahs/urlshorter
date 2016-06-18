from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView
from shorter.models import Link
# Create your views here.


class CreateLink(CreateView):
    model = Link
    fields = ['url']
    template_name = 'shorter/create_link.html'

    def form_valid(self, form):
        # Check if the Link object already exists
        prev = Link.objects.filter(url=form.instance.url)
        if prev:
            return redirect("shorter:link_show", pk=prev[0].pk)
        return super(CreateLink, self).form_valid(form)


class LinkShow(DetailView):
    model = Link
    template_name = 'shorter/detail_link.html'


